"""
$ pip3 install splinter
$ python3.5 getWebData.py
"""

from splinter import Browser

# Supported engine
# flag_skyscan = True

"""
Scrapping html from skyscanner
"""


def scrap_skyscan(browser_html):
    print(type(browser_html))


with Browser() as browser:

    flag_skyscan = True

    # Visit URL
    # url = "https://www.skyscanner.com.br/?currency=BRL&market=BR&\
    #    locale=pt-BR"
    url = "https://www.skyscanner.com.br/transporte/passagens-aereas/bvb/mao/\
181226/190104/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&\
cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=\
false&inboundaltsenabled=false&ref=home&currency=BRL&market=BR&\
locale=pt-BR&_mp=160121d4bd321-05ed7137a911b48-60217242-100200-\
160121d4bd6d8_1532527128465&rl:::true=&iF:::false=&enSort:::\
false=&dvflt:::=#results"

    # header-chosen-origin
    browser.visit(url)
    # browser.find_by_id('origin-fsc-search').fill('Manaus (MAO)')
    # browser.find_by_id('destination-fsc-search').fill('Boa Vista (BVB)')
    # browser.find_by_id('depart-fsc-datepicker-input').fill('Boa Vista (BVB)')
    # browser.find_by_id('depart-fsc-datepicker-input').fill('Boa Vista (BVB)')
    # Find the submit button and click
    # browser.find_by_text('Buscar').first.click()

    if browser.is_text_present('Receba alertas', wait_time=60):
        if browser.is_text_present('Recomendado', wait_time=60):
            # print(browser.html)
            browser.driver.save_screenshot("screen.png")
            if flag_skyscan:
                scrap_skyscan(browser.html)

    else:
        print("BUG :(")
        # browser.quit()
