from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    print()
    browser = chromium.launch()
    pass



with sync_playwright() as playwright:
    run(playwright)