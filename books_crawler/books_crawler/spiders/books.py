# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    # follow=Ture: recursively go into every link
    # deny_domains=('google.com'): do not go into this given domain
    rules = (Rule(LinkExtractor(deny_domains=('google.com')), callback='parse_page', follow=True),)
    # allow: only go into links contains the given string
    rules = (Rule(LinkExtractor(allow=('music')), callback='parse_page', follow=False),)

    def parse_page(self, response):
        yield {'URL': response.url}
