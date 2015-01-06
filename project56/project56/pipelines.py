# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
import json
from scrapy.conf import settings
from scrapy import log


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.Connection(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_COLLECTION']]

def process_item(self, item, spider):
    self.collection.insert(dict(item))

    filterEuro()

    def filterEuro():
        #    if u'\u20ac' in item["Price"]:

        log.msg("Item wrote to MongoDB database {}, collection {}, at host {}, port {}".format(
            settings['ds057000.mongolab.com'],
            settings['c_part'],
            settings['db_pcmaster'],
            settings['57000']))
    return item