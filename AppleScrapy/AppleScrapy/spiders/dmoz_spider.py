#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/8
import scrapy
from scrapy.spider import Spider

from AppleScrapy.items import DmozItem


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
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
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = DmozItem()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)
        return items
