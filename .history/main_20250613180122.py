from playwright.sync_api import sync_playwright, Playwright

expected_result = "Playwright"
url = "https://playwright.dev/"
testing_browser = ["firefox"]


def check_title_page(playwright:Playwright, url:url, result:expected_result):
    with sync_playwright() as playwright:
        



# def run(playwright: Playwright):
#     chromium = playwright.firefox
#     browser = chromium.launch()
#     print(url)
#     page = browser.new_page()
#     page.goto(url)
#     # title = page.title()
#     print(chromium.name)
#     print(page)
    
#     print("Заголовок страницы:", page.title())
#     browser.close()



    



# with sync_playwright() as playwright:
#     run(playwright)

