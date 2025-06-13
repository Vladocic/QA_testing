from playwright.sync_api import sync_playwright, Playwright

Expected_result = "Playwright"
url = "https://playwright.dev/"
# def check_title_page(playwright:Playwright):
#     with sync_playwright() as playwright:


def run(playwright: Playwright):
    chromium = playwright.firefox
    browser = chromium.launch()  
    page = browser.new_page().goto(url)
    title = page.title()
    print(chromium.name)
    
    print("Заголовок страницы:", page.title())
    browser.close()



    



with sync_playwright() as playwright:
    run(playwright)

