from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    pass



with sync_playwright() as playwright:
    run(playwright)