#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/8
import scrapy
from scrapy.spider import CrawlSpider, Rule

from AppleScrapy.items import QsbkItem
from scrapy.linkextractors import LinkExtractor

class DmozSpider(CrawlSpider):
    name = "qsbkcrawl"
    start_urls = [
        "http://www.qiushibaike.com"
    ]
    rules = [
        Rule(LinkExtractor(allow=('/8hr/page/[1-3]*')),callback='parse_list',follow=True)
    ]


    def parse_list(self, response):
        from scrapy import Selector
        sel = Selector(response)
        sites = sel.xpath('//*[@id="content-left"]/div[@class="article block untagged mb15"]')
        items = []
        print type(sites)
        for site in sites:
            item = QsbkItem()
            name = site.xpath('div[@class="content"]/text()').extract()
            nick = site.xpath('div[@class="author clearfix"]/a[2]/h2/text()').extract()
            item['desc'] = name
            item['nick'] = nick
            items.append(item)
        return items
