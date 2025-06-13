from playwright.sync_api import sync_playwright, Playwright

Expected_result = "Playwright"

def check

def run(playwright: Playwright):
    chromium = playwright.chromium
    print(chromium)
    browser = chromium.launch()  
    page = browser.new_page()
    a = page.goto("https://playwright.dev/")
    print(page.content())
    print("Заголовок страницы:", page.title())
    browser.close()


    



with sync_playwright() as playwright:
    run(playwright)

