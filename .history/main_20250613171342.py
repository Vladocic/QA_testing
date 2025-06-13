from playwright.sync_api import sync_playwright, Playwright,APIRequest

def run(playwright: Playwright):
    chromium = playwright.chromium
    print(chromium)
    APIRequest.new_context()
    pass



with sync_playwright() as playwright:
    run(playwright)