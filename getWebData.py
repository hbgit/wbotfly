"""
$ pip3 install splinter
$ python3.5 getWebData.py
"""

from splinter import Browser

with Browser() as browser:
    # Visit URL
    url = "https://www.skyscanner.com.br/?currency=BRL&market=BR&locale=pt-BR"
    # header-chosen-origin
    browser.visit(url)
    browser.find_by_id('origin-fsc-search').fill('Manaus (MAO)')
    browser.find_by_id('destination-fsc-search').fill('Boa Vista (BVB)')
    browser.find_by_id('depart-fsc-datepicker-input').fill('Boa Vista (BVB)')
    browser.find_by_id('depart-fsc-datepicker-input').fill('Boa Vista (BVB)')

    # Find the submit button and click
    browser.find_by_text('Buscar').first.click()

    if browser.is_text_present('Receba alertas', wait_time=60):
        flag_search = True
        while flag_search:
            print("Waiting ...")
            print(len(browser.find_by_id('header-list-count')))

            if len(browser.find_by_id('header-list-count')) == 0:
                flag_search = True
            else:
                flag_search = False

        browser.driver.save_screenshot("screen.png")
        browser.quit()
    else:
        print("BUG :(")
        browser.quit()
