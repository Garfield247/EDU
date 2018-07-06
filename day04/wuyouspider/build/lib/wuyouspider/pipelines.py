# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime

import redis
from twisted.internet.threads import deferToThread


class WuyouspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class WuyouJsonFile(object):
    def open_spider(self, spider):
        filename = '51job.json'
        self.fp = open(filename, 'w', encoding='utf-8')
        self.fp.write('[')

    def process_item(self, item, spider):
        obj = dict(item)
        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + ',\n')
        return item

    def close_spider(self, spider):
        self.fp.write(']')
        self.fp.close()

class SaveRedisPipline(object):
    def open_spider(self,spider):
        self.redis_cli = redis.Redis(host='192.168.3.116', port=6379, db=0)

    def process_item(self, item, spider, REDIS_KEY_DATA='crawl_data'):
        key = REDIS_KEY_DATA
        obj = dict(item)
        data = json.dumps(obj, ensure_ascii=False)
        self.redis_cli.rpush(key, data)
        return item
