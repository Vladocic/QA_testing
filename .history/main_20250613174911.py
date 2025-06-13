from playwright.sync_api import sync_playwright, Playwright

Expected_result = "Playwright"

# def check_title_page(playwright:Playwright):
#     with sync_playwright() as playwright:


def run(playwright: Playwright):
    chromium = playwright.firefox
    print(chromium)
    browser = chromium.launch()  
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    print(chromium.)
    print("Заголовок страницы:", page.title())
    browser.close()



    



with sync_playwright() as playwright:
    run(playwright)

