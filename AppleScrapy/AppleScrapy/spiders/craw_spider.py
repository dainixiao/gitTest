#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/8
from scrapy.spider import Spider
import scrapy
from AppleScrapy.items import DmozItem
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
class crawSpider(CrawlSpider):
    name = "crawt"
    start_urls = [
        "http://www.appledaily.com.tw/realtimenews/section/new/"
    ]
    rules = [
        Rule(LinkExtractor(allow=('/realtimenews/section/new/[1-3]$')),callback='parse_list',follow=True)
    ]

    def parse_list(self, response):
        print '1----------------------------------\n'
        domain = 'http://www.appledaily.com.tw'
        res = BeautifulSoup(response.body)
        print '3----------------------------------\n'
        for news in res.select('.rtddt'):
            print '4----------------------------------\n'
            yield scrapy.Request(domain+news.select('a')[0]['href'],self.parse_detail)

    def parse_detail(self,response):
        print '2----------------------------------\n'
        items = []
        res = BeautifulSoup(response.body)
        item = DmozItem()
        item['name'] = res.select('#h1')[0].text
        item['description'] = res.select('#summary')[0].text
        items.append(item)
        return items

