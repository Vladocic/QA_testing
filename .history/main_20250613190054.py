from playwright.sync_api import sync_playwright, Playwright

expected_result = "Fast and reliable end-to-end testing for modern web apps | Playwright"
url = "https://playwright.dev/"
browsers = ["chromium", "firefox", "webkit"]


def check_title_page(playwright:Playwright, url:str, result:str, browser_names:list[str]):
    with sync_playwright() as playwright:
        sucses_test = 0
        fail_test = 0
        steps = 0
        test_results = ""
        for browser_name in browser_names:
            steps+=1
            browser_type = getattr(playwright, browser_name)
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto(url)
            title = page.title()
            if browser_name == "chromium":
                title = "Manual error"
            if title == result:
                sucses_test+=1
                test_results+=f"✅  Проверка номер {steps} пройдена, браузер - {browser_type.name}, ожидаемый результат {result} свопадает с  фактическим {title}\n"
            else:
                fail_test+=1
                test_results+=f"❌ Провека номер {steps} не пройдена, браузер - {browser_type.name}, ожидаемый результат {result} НЕ соответсвует фактическому {title}\n"
        browser.close()
        test_results = f"Отчет по теситрвоанию:\n{test_results}\nИтоги тестирования:\nУспешных тестов {sucses_test}/{steps}\nНеуспешных тестов {fail_test}/{steps}" 

        print(test_results)
        return test_results


    with sync_playwright() as playwright:



        
check_title_page(playwright=Playwright ,url=url, result=expected_result, browser_names=browsers)





    


