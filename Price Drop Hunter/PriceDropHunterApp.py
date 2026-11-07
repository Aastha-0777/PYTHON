# ---------- 1. IMPORTS & SETTINGS ----------
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
import sqlite3
import datetime
import random
import time

BASE_URL = "https://books.toscrape.com"
PAGES_TO_SCRAPE = 2
DB_NAME = "prices.db"

# ---------- 2. DATABASE FUNCTIONS ----------

def create_table() : 
    pass

def save_products(products) : 
    pass

# ---------- 3. SCRAPING FUNCTIONS ----------


def clean_price(price_text):
    '''Removes the Currency Symbole from the text'''
    price = "".join(ch for ch in price_text if ch.isdigit() or ch == '.')
    return float(price)


def scrape_books(pages=PAGES_TO_SCRAPE):
    """Scrape books from the given number of pages. Returns a list of dicts."""
    products = []
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)

        for page_no in range(1, pages + 1):
            title = page.title()
            print("Page Title :", title)

            books_locator = page.locator("article.product_pod")
            # print(books_locator)
            for i in range(books_locator.count()):
                book = books_locator.nth(i)
                book_title = book.locator("h3 a").get_attribute("title")
                price = clean_price(book.locator(".price_color").inner_text())
                link = urljoin(page.url, book.locator("h3 a").get_attribute("href"))
                
                products.append({
                    "name": book_title,
                    "price": price,
                    "url": link
                })
                
                # print(
                #     f'Title : {book_title} | Price : {price} | Link : {link}')
                # print(
                #     '------------------------------------------------------------------------------------------------')

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

# ---------- 5. GUI ----------

# ---------- 6. RUN THE APP ----------


def main():
    products_list = scrape_books()
    print(f"Scraped {len(products_list)} products")
    for i in products_list : 
        print(i)

if __name__ == '__main__':
    main()
