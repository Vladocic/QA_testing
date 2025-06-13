from playwright.sync_api import sync_playwright, Playwright

expected_result = "Fast and reliable end-to-end testing for modern web apps | Playwright"
url = "https://playwright.dev/"
browsers = ["chromium", "firefox", "webkit"]


def check_title_page(playwright:Playwright, url:str, result:str, browser_names:list[str]):
    with sync_playwright() as playwright:
        sucses_test = 0
        fail_test = 0
        result_test = ""
        for browser_name in browser_names:
            browser_type = getattr(playwright, browser_name)
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto(url)
            title = page.title()
            if browser_name == "chromium":
                title = "1"
            if title == result:
                sucses_test+=1
                result_test+=f"✅  Проверка пройдена, браузер - {browser_type.name}, ожидаемый результат {result} свопадает с  фактическим {title}\n"
            else:
                fail_test+=1
                result_test+=f"❌ Провека не пройдена, браузер - {browser_type.name}, ожидаемый результат {result} НЕ соответсвует фактическому {title}\n"
 
        print(result_test)
        print(sucses_test)
        pass

def show_test_result(sucses_test,fail_test):
    if sucses_test



        
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

