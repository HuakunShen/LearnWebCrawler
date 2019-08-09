# -*- coding: utf-8 -*-
import scrapy
from scrapy_items_example.items import ScrapyItemsExampleItem

class SampleItemsSpiderSpider(scrapy.Spider):
    name = 'sample_items_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        authors = response.xpath('//*[@itemprop="author"]/text()').extract()
        # using yield is the alternative, now we are learning to use items. There is a difference in terms of data display
        # yield {'authors': authors}
        item = ScrapyItemsExampleItem()
        item['authors'] = authors
        return item
        
 