# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class TianqiItem(scrapy.Item):
    shengfenName = scrapy.Field()
    shiquName = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    date = scrapy.Field()
    weather = scrapy.Field()


class Shengfen(scrapy.Item):
    shengfenURL = scrapy.Field()


class ShiquItem(scrapy.Item):
    shiquURL = scrapy.Field()

