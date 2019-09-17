# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class TianqiPipeline(object):
    def process_item(self, item, spider):
        return item


class MojiPipeline(object):
    def process_item(self, item, MojiSpider):
        keyA = item["shengfenName"][0] + item["shiquName"][0]
        itemdict = {}
        datelist = item["date"]
        weatherlist = item["weather"]
        highlist = item["high"]
        lowlist = item["low"]
        for num in range(len(datelist)):
            itemdict[datelist[num]] = list([weatherlist[num], highlist[num], lowlist[num]])
        item = {keyA: itemdict}
        yield item


class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url = crawler.settings.get('MONGO_URL'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()