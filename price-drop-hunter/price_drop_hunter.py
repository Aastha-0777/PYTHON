# ---------- 1. IMPORTS & SETTINGS ----------
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
import sqlite3
import datetime
import random
import time
from tkinter import ttk
import tkinter as tk

BASE_URL = "https://books.toscrape.com"
PAGES_TO_SCRAPE = 2
DB_NAME = "prices.db"

# ---------- 2. DATABASE FUNCTIONS ----------


def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # creates table products
    cur.execute("""            
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE
        )
    """)

    # creates table prices

    cur.execute("""
        CREATE TABLE IF NOT EXISTS prices(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            price REAL NOT NULL,
            scraped_at TEXT NOT NULL, 
            FOREIGN KEY (product_id) REFERENCES products(id)            
        )
    """)

    conn.commit()
    conn.close()


def save_products(products):
    conn = sqlite3.connect(DB_NAME)
    try:
        cur = conn.cursor()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for item in products:
            cur.execute("INSERT OR IGNORE INTO products (name, url) VALUES (?, ?)",
                        (item["name"], item["url"]))
            cur.execute("SELECT id FROM products WHERE url = ?", (item["url"],))
            p_id = cur.fetchone()[0]
            cur.execute("INSERT INTO prices (product_id, price, scraped_at) VALUES (?, ?, ?)",
                        (p_id, item["price"], now))

        conn.commit()
    except Exception:
        conn.rollback()      # undo the half-saved scrape
        raise                # let refresh_data show the error
    finally:
        conn.close()         # always runs, even after an error

# ---------- 3. SCRAPING FUNCTIONS ----------


def clean_price(price_text):
    '''Removes the Currency Symbole from the text'''
    price = "".join(ch for ch in price_text if ch.isdigit() or ch == '.')
    return float(price)


def scrape_books(pages=PAGES_TO_SCRAPE):
    """Scrape books from the given number of pages. Returns a list of dicts."""
    products = []
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)

        for page_no in range(1, pages + 1):
            title = page.title()
            print("Page Title :", title)

            books_locator = page.locator("article.product_pod")
            for i in range(books_locator.count()):
                book = books_locator.nth(i)
                book_title = book.locator("h3 a").get_attribute("title")
                price = clean_price(book.locator(".price_color").inner_text())
                link = urljoin(page.url, book.locator(
                    "h3 a").get_attribute("href"))

                products.append({
                    "name": book_title,
                    "price": price,
                    "url": link
                })
                
            print(f"Page {page_no} done")

            next_btn = page.locator(".next a")
            if page_no < pages and next_btn.count() > 0:
                next_btn.click()
                page.wait_for_load_state("domcontentloaded")
                time.sleep(random.uniform(1, 2))   # polite delay
            else:
                break

        browser.close()

    return products

# ---------- 4. PRICE LOGIC ----------


def get_price_changes():
    """Returns a list of dicts: name, previous, current, change."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    results = []

    cur.execute("SELECT id, name FROM products")
    all_products = cur.fetchall()

    for product_id, name in all_products:
        cur.execute("""
            SELECT price FROM prices
            WHERE product_id = ?
            ORDER BY id DESC
            LIMIT 2
        """, (product_id,))
        prices = cur.fetchall()
        if not prices:
            continue
        
        current = prices[0][0]
        if len(prices) > 1:
            previous = prices[1][0]
            change = round(current - previous, 2)
        else:                      
            previous = None
            change = None
        
        results.append({
            "name"     : name,
            "previous" : previous,
            "current"  : current,
            "change"   : change
        })
        
    conn.close()
    return results


def find_drops(changes):
    return [c for c in changes if c["change"] is not None and c["change"] < 0]

def refresh_data():
    """Scrape, save, compare. Returns (changes, status_message)."""
    try:
        products = scrape_books()
        if not products:
            raise Exception("No products found - the site layout may have changed")
        save_products(products)
        changes = get_price_changes()
        drops = find_drops(changes)
        return changes, f"Scraped {len(products)} products. {len(drops)} price drops found."
    except Exception as e:
        return get_price_changes(), f"Error: {e}"

# ---------- 5. GUI ----------

# colours in one place, so the look is easy to change
BG = "#f3f4f6"
DARK = "#1f2937"
BLUE = "#2563eb"
GREEN_BG = "#d1fae5"
GREEN_FG = "#047857"
RED_FG = "#b91c1c"


def format_price(value):
    """51.77 -> '£51.77', None -> '-'"""
    return "-" if value is None else f"£{value:.2f}"


def format_change(value):
    """Arrow + amount, so you can read the change at a glance."""
    if value is None:
        return "-"
    if value < 0:
        return f"▼ £{abs(value):.2f}"
    if value > 0:
        return f"▲ £{value:.2f}"
    return "no change"


def fill_table(tree, changes, search_text=""):
    tree.delete(*tree.get_children())                 # clear old rows

    # keep only names that contain the search text (ignoring upper/lower case)
    shown = [c for c in changes if search_text.lower() in c["name"].lower()]
    # biggest drops first (most negative change), None counts as 0
    shown.sort(key=lambda c: (c["change"] or 0, c["name"]))

    for i, c in enumerate(shown):
        tags = ["even" if i % 2 == 0 else "odd"]      # striped rows
        if c["change"] is not None and c["change"] < 0:
            tags.append("drop")
        elif c["change"] is not None and c["change"] > 0:
            tags.append("rise")

        tree.insert("", "end", values=(
            c["name"],
            format_price(c["previous"]),
            format_price(c["current"]),
            format_change(c["change"]),
        ), tags=tags)


def build_gui():
    root = tk.Tk()
    root.title("Price Drop Hunter")
    root.geometry("900x620")
    root.minsize(700, 450)
    root.configure(bg=BG)

    # ----- table look -----
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", rowheight=28, font=("Arial", 10))
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"),
                    background=DARK, foreground="white")
    style.map("Treeview.Heading", background=[("active", "#374151")])

    # ----- header banner -----
    header = tk.Frame(root, bg=DARK)
    header.pack(fill="x")
    tk.Label(header, text="Price Drop Hunter", font=("Arial", 18, "bold"),
             bg=DARK, fg="white").pack(anchor="w", padx=20, pady=(12, 0))
    tk.Label(header, text="Track book prices and catch the drops",
             font=("Arial", 10), bg=DARK, fg="#9ca3af").pack(anchor="w", padx=20, pady=(0, 12))

    # ----- three summary cards -----
    cards = tk.Frame(root, bg=BG)
    cards.pack(fill="x", padx=20, pady=12)

    def make_card(title):
        card = tk.Frame(cards, bg="white", padx=16, pady=8)
        card.pack(side="left", expand=True, fill="x", padx=5)
        tk.Label(card, text=title, font=("Arial", 9),
                 bg="white", fg="#6b7280").pack(anchor="w")
        value = tk.Label(card, text="-", font=("Arial", 18, "bold"),
                         bg="white", fg=DARK)
        value.pack(anchor="w")
        return value

    total_lbl = make_card("Products tracked")
    drops_lbl = make_card("Price drops")
    updated_lbl = make_card("Last updated")

    # ----- search box + refresh button -----
    toolbar = tk.Frame(root, bg=BG)
    toolbar.pack(fill="x", padx=25)
    tk.Label(toolbar, text="Search:", bg=BG, font=("Arial", 10)).pack(side="left")
    search_var = tk.StringVar()
    tk.Entry(toolbar, textvariable=search_var, width=30,
             font=("Arial", 10)).pack(side="left", padx=8)
    refresh_btn = tk.Button(toolbar, text="Refresh", bg=BLUE, fg="white",
                            font=("Arial", 10, "bold"), relief="flat",
                            padx=16, pady=4, command=lambda: on_refresh())
    refresh_btn.pack(side="right")

    # ----- status bar (packed before the table so it never gets squeezed out) -----
    status = tk.Label(root, text="Ready", anchor="w", bg="#e5e7eb",
                      font=("Arial", 9), padx=10, pady=4)
    status.pack(side="bottom", fill="x")

    # ----- table with scrollbar -----
    table_frame = tk.Frame(root)
    table_frame.pack(fill="both", expand=True, padx=25, pady=10)

    columns = ("Name", "Previous", "Current", "Change")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings")
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    for col in columns:
        tree.heading(col, text=col)
    tree.column("Name", width=420, anchor="w")
    for col in ("Previous", "Current", "Change"):
        tree.column(col, width=110, anchor="e")

    # row colours: later tags win, so "drop" and "rise" override the stripes
    tree.tag_configure("even", background="#ffffff")
    tree.tag_configure("odd", background="#f3f4f6")
    tree.tag_configure("drop", background=GREEN_BG, foreground=GREEN_FG)
    tree.tag_configure("rise", foreground=RED_FG)

    # ----- behaviour -----
    data = {"changes": []}          # a dict, so the functions below can change it

    def redraw():
        fill_table(tree, data["changes"], search_var.get())
        drops = find_drops(data["changes"])
        total_lbl.config(text=str(len(data["changes"])))
        drops_lbl.config(text=str(len(drops)),
                         fg=GREEN_FG if drops else DARK)

    def on_refresh():
        refresh_btn.config(state="disabled", text="Scraping...")
        status.config(text="Scraping... please wait")
        root.update()                                   # show the message before the freeze

        changes, message = refresh_data()
        data["changes"] = changes
        if not message.startswith("Error"):
            updated_lbl.config(text=datetime.datetime.now().strftime("%H:%M"))
        redraw()

        status.config(text=message)
        refresh_btn.config(state="normal", text="Refresh")

    search_var.trace_add("write", lambda *args: redraw())   # filter as you type

    data["changes"] = get_price_changes()                   # show saved data on startup
    redraw()
    root.mainloop()
    

# ---------- 6. RUN THE APP ----------


def main():
    create_tables()
    build_gui()

if __name__ == '__main__':
    main()
