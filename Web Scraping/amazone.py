from playwright.sync_api import sync_playwright

url = "https://www.amazon.in/"
product ={}
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    
    # searchbar_locator = page.locator("div.nav-search-field")
    searchbar_locator = page.locator("#twotabsearchtextbox")
    # searchbar_locator = page.get_by_text("Search Amazon.in", exact=True).first
    # page.wait_for_selector('div[id = "nav-search"]')
    searchbar_locator.fill("Laptops Under 35K")
    searchbar_locator.press("Enter")
    
    page.wait_for_load_state("networkidle")

    page.wait_for_timeout(3000)
    
    laptops = page.locator(".s-main-slot")
    
    print(laptops)
    
    browser.close()

