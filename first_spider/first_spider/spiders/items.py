import scrapy

class QuotesSpiderItem(scrapy.item):
    h1_tag = scrapy.Field()
    tags = scrapy.Field()