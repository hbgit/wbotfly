"""
$ docker pull scrapinghub/splash
$ docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash

http://localhost:8050/

pip install scrapy-splash

To put our spider to work, go to the project’s top level
directory and run:

$ scrapy crawl skyscan

"""

import scrapy
from scrapy_splash import SplashRequest


# from skyscan_item import SkyScanScraperItem

class SkyScanScraperItem(scrapy.Item):
    company = scrapy.Field()
    price = scrapy.Field()
    # time_* is a list where the first data is GO and second
    # is return
    time_go = scrapy.Field()
    time_return = scrapy.Field()


class SkyScanSpider(scrapy.Spider):
    name = "skyscan"
    # company = scrapy.Field()
    # price = scrapy.Field()
    # download_delay = 5.0

    def start_requests(self):
        urls = [
            'https://www.skyscanner.com.br/transporte/\
passagens-aereas/bvb/mao/181226/190104/?\
adults=1&children=0&adultsv2=1&childrenv2=&\
infants=0&cabinclass=economy&rtn=1&preferdirects=\
false&outboundaltsenabled=false&inboundaltsenabled=\
false&ref=home&currency=BRL&market=BR&locale=pt-BR&\
_mp=160121d4bd321-05ed7137a911b48-60217242-100200\
-160121d4bd6d8_1532527128465&rl:::true=&iF:::false=&\
enSort:::false=&dvflt:::=#results'
        ]

        for url in urls:
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.html',
                                meta={'solve_captcha': True},
                                args={'wait': 0.5}
                                )

    def parse(self, response):
        # response.body is a result of render.html call; it
        # contains HTML processed by a browser.
        for block_op in response.css('li.day-list-item'):
            self.log("Checking block prices...")
            # print(block_op.css)
            item = SkyScanScraperItem()

            item['company'] = block_op.css(
                        'div.ItineraryContent__group-logo-DYQgf\
                        span.AirlineLogo__airline-text-7EJ0z::text'
                      ).extract()

            if not bool(item['company']):
                # big-logo AirlineLogo__big-logo-22gjJ
                item['company'] = block_op.css(
                        'div.big-logo\
                        img::attr(title)'
                      ).extract_first()

            item['price'] = block_op.css(
                        'div.CTASection__price-horizontal-1syz1\
                         a.CTASection__price-2bc7h::text'
                    ).extract()

            item['time_go'] = block_op.css(
                'div.LegInfo__leg-depart-3GMlb\
                span.LegInfo__times-Qn_ji::text'
            ).extract()

            item['time_return'] = block_op.css(
                'div.LegInfo__leg-arrive-1spXx\
                span.LegInfo__times-Qn_ji::text'
            ).extract()

            yield item

        """
        filename = "test.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        """
