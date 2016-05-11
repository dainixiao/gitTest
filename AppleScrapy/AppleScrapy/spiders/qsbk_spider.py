#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/8
import scrapy
from scrapy.spider import Spider

from AppleScrapy.items import DmozItem, QsbkItem


class DmozSpider(Spider):
    name = "qsbk"
    allowed_domains = ["qiushibaike.com"]
    start_urls = [
        "http://www.qiushibaike.com/8hr/page/1?s=4876297"
    ]

    # def parse(self, response):
    #     for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
    #         url = response.urljoin(response.url, href.extract())
    #         yield scrapy.Request(url, callback=self.parse_dir_contents)
    #
    # def parse_dir_contents(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         item = DmozItem()
    #         item['title'] = sel.xpath('a/text()').extract()
    #         item['link'] = sel.xpath('a/@href').extract()
    #         item['desc'] = sel.xpath('text()').extract()
    #         yield item



    def parse(self, response):
        # for sel in response.xpath('//ul/li'):
        #     title = sel.xpath('a/text()').extract()
        #     link = sel.xpath('a/@href').extract()
        #     desc = sel.xpath('text()').extract()
        #     print title, link, desc
        # filename = response.url.split("/")[-2]
        # open(filename, 'wb').write(response.body)
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
