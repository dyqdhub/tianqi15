# -*- coding: utf-8 -*-
import scrapy
from ..items import TianqiItem
from ..items import Shengfen
from ..items import ShiquItem

class MojiSpider(scrapy.Spider):
    name = 'moji'
    allowed_domains = ['tianqi.moji.com']
    start_urls = ['https://tianqi.moji.com/forecast15/china']
    mojiurl = 'https://tianqi.moji.com'

    def parse_data(self, response):
        item = TianqiItem()
        item['shengfenName'] = response.xpath('//*[@id="detail"]/div[1]/div/ul/li[3]/a/text()').extract()
        item['shiquName'] = response.xpath('//*[@id="detail"]/div[1]/div/ul/li[4]/text()').extract()
        item['date'] = response.xpath('//*[@id="detail_future"]/div[2]/div[2]/ul/li/span[6]/text()').extract()
        item['weather'] = response.xpath('//*[@id="detail_future"]/div[2]/div[2]/ul/li/span[5]/text()').extract()
        item['high'] = response.xpath('//*[@id="detail_future"]/div[2]/div[2]/ul/li/div/p/b/text()').extract()
        item['low'] = response.xpath('//*[@id="detail_future"]/div[2]/div[2]/ul/li/div/p/strong/text()').extract()
        yield item


    def parse_shiqu(self, response):
        shiqulist = response.xpath('//*[@id="city"]/div[2]/div[2]/ul/li/a/@href').extract()
        for shiquURL in shiqulist:
            yield scrapy.Request(url=shiquURL, callback=self.parse_data)


    def parse(self, response):
        shengfenlist = response.xpath('//div[@id="city"]/div[2]/dl/dd/ul/li/a/@href').extract()
        # item = Shengfen()
        for shengfenurl in shengfenlist:
            shengfenURL = self.mojiurl + shengfenurl
            # item['shengfenURL'] = shengfenURL
            # yield item
            yield scrapy.Request(url=shengfenURL, callback=self.parse_shiqu)
