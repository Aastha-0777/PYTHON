from playwright.sync_api import sync_playwright

products = {}

with sync_playwright() as p : 
    #if headless = True -> browser preview will run in background and not visible to us
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://books.toscrape.com/")
    # page.wait_for_timeout(4000)
    title = page.title()
    print("Page Title :", title)

    books = page.locator("article.product_pod")

    print(books)
    for i in range(books.count()):
        book = books.nth(i)
        title = book.locator("h3 a").get_attribute("title")
        price = book.locator(".price_color").inner_text()
        availabilty = book.locator(".instock").inner_text()

        products[i] = [{"title" : title, "avi." : availabilty, "price" : price}]    

    browser.close()

print(products)