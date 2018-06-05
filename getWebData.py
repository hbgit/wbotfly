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

    if browser.is_text_present('Recomendados', wait_time=60):
        print("Searching done")
    else:
        print("BUG :(")
