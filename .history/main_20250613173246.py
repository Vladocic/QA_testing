from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    print(chromium)
    browser = chromium.launch(headless=False)  
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    print("Заголовок страницы:", page.title())
    input("Нажмите Enter, чтобы закрыть браузер...")


    



with sync_playwright() as playwright:
    run(playwright)

