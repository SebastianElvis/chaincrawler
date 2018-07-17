# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoneroTransaction(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    block_height = scrapy.Field()
    transaction_hash = scrapy.Field()
    outputs = scrapy.Field()
    fee = scrapy.Field()
    ringsize = scrapy.Field()
    in_count = scrapy.Field()
    out_count = scrapy.Field()
    size = scrapy.Field()
    version = scrapy.Field()


class BytecoinTransaction(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    block_height = scrapy.Field()
    transaction_hash = scrapy.Field()
    outputs = scrapy.Field()
    fee = scrapy.Field()
    ringsize = scrapy.Field()
    in_count = scrapy.Field()
    out_count = scrapy.Field()
    size = scrapy.Field()
    version = scrapy.Field()