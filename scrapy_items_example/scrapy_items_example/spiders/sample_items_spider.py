# -*- coding: utf-8 -*-
import scrapy


class SampleItemsSpiderSpider(scrapy.Spider):
    name = 'sample_items_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        authors = response.xpath("")
        yield {
            'author': authors
        }
 