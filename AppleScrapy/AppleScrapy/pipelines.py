# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class ApplescrapyPipeline(object):

    def open_spider(self,spider):
        self.connction = pymongo.Connection("192.168.1.104", 27017)
        db_auth = self.connction.admin
        db_auth.authenticate('root', '123456')
        self.douqu = self.connction.douqu
        pass
    def close_spider(self,spider):
        self.connction.close()
        pass
    def process_item(self, item, spider):
        self.douqu.haha.insert(dict(item))
        return item


class AppleCrawlScrapyPipeline(object):
    def open_spider(self, spider):
        self.connction = pymongo.Connection("192.168.1.104", 27017)
        db_auth = self.connction.admin
        db_auth.authenticate('root', '123456')
        self.douqu = self.connction.douqu
        pass

    def close_spider(self, spider):
        self.connction.close()
        pass

    def process_item(self, item, spider):
        self.douqu.wuwuw.insert(dict(item))
        return item
