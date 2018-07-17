# -*- coding: utf-8 -*-

import scrapy
from ..items import MoneroTransaction

class MoneroSpider(scrapy.Spider):
    name = 'monero'
    
    def start_requests(self):
        last_height = 1618540
        for i in range(200000):
            height = last_height - i
            url = 'https://xmrchain.net/block/' + str(height)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        transaction_elems = response.xpath('//table[3]/tr')
        if len(transaction_elems) == 1:
            return
        transaction_elems.remove(transaction_elems[0])
        for elem in transaction_elems:
            transaction = MoneroTransaction()
            transaction['block_height'] = int(response.url.split('/')[-1])
            transaction['transaction_hash'] = elem.xpath('td[1]/a/text()').extract()[0]
            
            outputs = elem.xpath('td[2]/text()').extract()[0]
            if outputs == '?':
                transaction['outputs'] = -1
            else:
                transaction['outputs'] = float(outputs)
            
            transaction['fee'] = float(elem.xpath('td[3]/text()').extract()[0])
            transaction['ringsize'] = int(elem.xpath('td[4]/text()').extract()[0])
            
            inout = elem.xpath('td[5]/text()').extract()[0]
            transaction['in_count'] = int(inout.split('/')[0])
            transaction['out_count'] = int(inout.split('/')[1])
            
            transaction['size'] = float(elem.xpath('td[6]/text()').extract()[0])
            transaction['version'] = int(elem.xpath('td[7]/text()').extract()[0])
            
            yield transaction
            
            