import scrapy


class SkyScanScraperItem(scrapy.Item):
    company = scrapy.Field()
    price = scrapy.Field()
    # developer = scrapy.Field()
