# -*- coding: utf-8 -*-

import scrapy
import json
from ..items import BytecoinTransaction

class BytecoinSpider(scrapy.Spider):
    name = 'bytecoin'
    
    def start_requests(self):
        last_height = 1529430
        txs_per_request = 10
        for i in range(200000/txs_per_request):
            start = last_height - (i+1)*txs_per_request
            end = last_height - i*txs_per_request
            url = 'https://chainradar.com/api/v1/bcn/blocks/range/%d/%d/full' % (start, end)
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        json_blocks = json.loads(response.body_as_unicode())
        for json_block in json_blocks:
            print "hellooooooooooooooooooooo", json_block
            if json_block['blockHeader']['txCount'] == 0:
                continue
            
            block_height = json_block['blockHeader']['height']
            for json_tx in json_block['transactions']:
                transaction = BytecoinTransaction()
                transaction['block_height'] = block_height
                transaction['transaction_hash'] = json_tx['hash']
                transaction['outputs'] = -1
                transaction['fee'] = json_tx['fee']
                transaction['ringsize'] = json_tx['mixin']
                transaction['in_count'] = json_tx['inputsCount']
                transaction['out_count'] = json_tx['outputsCount']
                transaction['size'] = json_tx['size']
                transaction['version'] = -1
                
                yield transaction
