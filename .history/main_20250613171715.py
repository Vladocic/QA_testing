from playwright.sync_api import sync_playwright, Playwright,APIRequest

def run(playwright: Playwright):
    chromium = playwright.chromium
    print(chromium)

    pass



with sync_playwright() as playwright:
    run(playwright)