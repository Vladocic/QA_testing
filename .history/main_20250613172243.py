from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    print(chromium)
    browser = chromium.launch()    
    page = browser.new_page()
    page.goto("https://playwright.dev/")
        print("Заголовок страницы:", page.title())

    



with sync_playwright() as playwright:
    run(playwright)

