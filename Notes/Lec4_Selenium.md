# Lec4 Selenium

install selenium: `pip install selenium`

google chromeDriver and download it

```python
# # -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
class SeleniumbooksSpider(Spider):
    name = 'seleniumBooks'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('/home/hacker/Documents/CS_Projects/web_crawler_learning/chromedriver')
        self.driver.get('http://books.toscrape.com')

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:
            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse_book)

    def parse_book(self, response):
        pass


```

## click next button on page

iterate over pages and get info from each page

```python
# # -*- coding: utf-8 -*-
from time import sleep
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException
class SeleniumbooksSpider(Spider):
    name = 'seleniumBooks'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('/home/hacker/Documents/CS_Projects/web_crawler_learning/chromedriver')
        self.driver.get('http://books.toscrape.com')

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:
            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse_book)
        while True:
            try:
                next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
                sleep(3)
                self.logger.info('Sleeping for 3 seconds')
                next_page.click()
                sel = Selector(text=self.driver.page_source)
                books = sel.xpath('//h3/a/@href').extract()
                for book in books:
                    url = 'http://books.toscrape.com/catalogue/' + book
                    yield Request(url, callback=self.parse_book)
            except NoSuchElementException:
                self.logger.info('No more Pages to Load')
                self.driver.quit()
                break

    def parse_book(self, responsebreak):
        pass


```

