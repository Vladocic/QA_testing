from playwright.sync_api import sync_playwright, Playwright

expected_result = "Fast and reliable end-to-end testing for modern web apps | Playwright"
url = "https://playwright.dev/"
browsers = ["chromium", "firefox", "webkit"]


def check_title_page(playwright:Playwright, url:str, result:str, browser_names:list[str]):
    with sync_playwright() as playwright:
        sucses_test = 0
        result_test = ""
        for browser_name in browser_names:
            browser_type = getattr(playwright, browser_name)
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto(url)
            title = page.title()
            if title == result:
                result_test+=


            test_pass = f"✅  Проверка пройдена, браузер - {browser_type.name}, ожидаемый результат {result} свопадает с  фактическим {title}"
            test_fail = f"❌ Провека не пройдена, браузер - {browser_type.name}, ожидаемый результат {result} НЕ соответсвует фактическому {title}"
            
            print(test_pass if title == result else test_fail)
            


            pass



        
check_title_page(playwright=Playwright ,url=url, result=expected_result, browser_names=browsers)



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

