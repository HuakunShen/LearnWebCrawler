# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class GrabbingurlsbooksSpider(Spider):
    name = 'grabbingURLsBooks'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        pass
