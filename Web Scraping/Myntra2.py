from playwright.sync_api import sync_playwright

url = "https://www.myntra.com/men-tshirts"
product ={}
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    
    searchbar_locator = page.locator(".desktop-searchBar")
    searchbar_locator.fill("Nike T-shirt")
    searchbar_locator.press("Enter")

    page.wait_for_timeout(3000)
    browser.close()

