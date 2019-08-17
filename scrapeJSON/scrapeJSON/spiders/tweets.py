# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.http import FormRequest


class TweetsSpider(scrapy.Spider):
    name = 'tweets'
    allowed_domains = ['trumptwitterarchive.com']
    def __init__(self):
        self.start_urls = ['https://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2016.json',
                  'https://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2017.json']

    def parse(self, response):
        json_response = json.loads(response.body)
        for tweet in json_response:
            yield {
                "source": tweet['source'],
                "id_str": tweet['id_str'],
                "text": tweet['text'],
                "created_at": tweet['created_at'],
                "retweet_count": tweet['retweet_count'],
                "in_reply_to_user_id_str": tweet['in_reply_to_user_id_str'],
                "favorite_count": tweet['favorite_count'],
                "is_retweet": tweet['is_retweet']
            }


# data = {
#     "org": "",
#     "code": "CSC",
#     "section": "",
#     "studyyear": "",
#     "daytime": "",
#     "weekday": "",
#     "prof": "",
#     "breadth": "",
#     "online": "",
#     "waitlist": "",
#     "available": "",
#     "title": ""}
# page = FormRequest(url='https://timetable.iit.artsci.utoronto.ca/api/20199/courses', formdata=data, method='GET')
