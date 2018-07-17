# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from items import MoneroTransaction, BytecoinTransaction

class MongoPipeline(object):
    monero_collection = 'monero'
    bytecoin_collection = 'bytecoin'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = '127.0.0.1'
        self.mongo_db = 'blockchain'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, MoneroTransaction):
            self.db[self.monero_collection].insert_one(dict(item))
        elif isinstance(item, BytecoinTransaction):
            self.db[self.bytecoin_collection].insert_one(dict(item))
        return item
