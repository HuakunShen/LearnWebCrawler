# -*- coding: utf-8 -*-
import scrapy


class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['classcentral.com']
    start_urls = ['http://classcentral.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            subject_url = response.xpath('//*[contains(@title, "' + self.subject + '")]/@href').extract_first()
            yield scrapy.http.Request(response.urljoin(subject_url), callback=self.parse_subject)
        else:
            self.logger.info('Scraping all Subjects.')
            self.subjects = response.xpath('//*[@class="text--blue"]/@href').extract()
            for subject in self.subjects:
                yield scrapy.http.Request(response.urljoin(subject), callback=self.parse_subject)
        
    def parse_subject(self, response):
        subject_name = response.xpath('//*[@class="head-2 medium-up-head-1 text--bold"]/text()').extract_first()

        courses = response.xpath('//*[@class="text--charcoal text-2 medium-up-text-1 block course-name"]')
        for course in courses:
            course_name = course.xpath('.//@title').extract_first()
            course_url = course.xpath('.//@href').extract_first()
            abs_course_url = response.urljoin(course_url)

            yield {
                "subject_name": subject_name,
                "course_name": course_name,
                "abs_course_url": abs_course_url
            }

        next_page = response.xpath('//*[@rel="next"]/@href').extract_first()
        abs_next_page = response.urljoin(next_page)
        yield scrapy.http.Request(abs_next_page, callback=self.parse_subject)
        