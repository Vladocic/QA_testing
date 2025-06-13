from playwright.sync_api import sync_playwright, Playwright

expected_result = "Playwright"
url = "https://playwright.dev/"
browsers = ["chromium", "firefox", "webkit"]


def check_title_page(playwright:Playwright, url:str, result:str, browsers:list[str]):
    with sync_playwright() as playwright:
        for browser_name in browsers:
            browser_type = getattr(playwright, browser)
            browser_type.launch()
            page = browser_type.new_page()
            page.goto(url)
            print(page.title)
            # print(browser_type.name)

            pass



        
check_title_page(playwright=Playwright ,url=url, result=expected_result, browsers=browsers)



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

