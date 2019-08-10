# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from pymongo import MongoClient
# from scrapy.crawler import settings
# from scrapy import settings

class MongoDBPipeline(object):

    def __init__(self):
        self.connection = MongoClient(
            'localhost',
            27017
        )
        db = self.connection['books']
        self.collection = db['products']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    