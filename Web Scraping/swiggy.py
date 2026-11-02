from playwright.sync_api import sync_playwright

with sync_playwright() as p :
    
    browser = p.chromium.launch(
        headless=False,
        channel="chrome",   # uses your installed Google Chrome; remove this line if you don't have it
        args=["--disable-blink-features=AutomationControlled"])
    context = browser.new_context(
        viewport={"width": 1366, "height": 768},
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        ),
        locale="en-IN",
    )
    page = context.new_page()

    page.goto("https://www.swiggy.com/", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(7000)                      # let the page draw first
    print("Title:", page.title())

    navabar_container_locator = page.locator('a[href*="instamart"]').first
    
    if navabar_container_locator:
        navabar_container_locator.click()
        page.wait_for_timeout(5000)
        page.wait_for_load_state("domcontentloaded")
        
        # 1. Target the <img> inside the div with the specific data-testid
        fresh_fruits_locator = page.get_by_text("Fresh Fruits", exact=True).first
        fresh_fruits_locator.scroll_into_view_if_needed()
        fresh_fruits_locator.click()
        page.wait_for_timeout(5000)
        
        fruits = page.wait_for_selector('div[data-testid="item-collection-card-full"]')
        print(fruits)
        
    else :
        print("no class located..")    

    browser.close()