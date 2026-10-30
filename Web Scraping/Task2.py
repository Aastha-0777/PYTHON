from playwright.sync_api import sync_playwright
import random as r

products = {}

with sync_playwright() as p : 

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.myntra.com/men-tshirts")

    # page.wait_for_event("domcontentloaded")
    j = 0
    next_btn = page.locator(".pagination-next")
    for i in range(1, 10) : 
        if next_btn.count() and next_btn.is_enabled() : 
            next_btn.click()
            # page.wait_for_timeout(4000)
        
            title = page.title()
            print("Page Title :", title)
                        
            tshirts = page.locator("li.product-base")
            print(tshirts)            
            for i in range(tshirts.count()) : 
                tshirt = tshirts.nth(i)
                brand = tshirt.locator("h3.product-brand").inner_text()
                # print(brand)
                discription = tshirt.locator("h4.product-product").inner_text()
                # print(discription)
                price_locator = tshirt.locator("span.product-strike")
                price = price_locator.inner_text() if price_locator.count() > 0 else "N/A"
                dis_price_locator = tshirt.locator("span.product-discountedPrice")
                dis_price = dis_price_locator.inner_text() if dis_price_locator.count() > 0 else "N/A"
                # print(price)
                products[j] = [{"Brand" : brand, "Discription" : discription, "Original Price" : price ,"Discounted Price" : dis_price}]
                j += 1
        else : 
            print("Button Not Available...")
        
    browser.close()         

print(len(products))
for i in products : 
    print(products[i])
