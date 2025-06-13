from playwright.sync_api import sync_playwright, Playwright,APIRequest

def run(playwright: Playwright):
    chromium = playwright.chromium
    print(chromium)
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    browser.close()
    



with sync_playwright() as playwright:
    run(playwright)

sync_playwright()