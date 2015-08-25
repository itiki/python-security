# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

def dict_plus(dict_one, dict_two):
    for key, value in dict_one.items():
        if key in dict_two.keys():
                dict_two[key] += dict_one[key]
        else:
                dict_two[key] = dict_one[key]
    return dict_two

class GubaPipeline(object):
    MONGODB_SERVER = '192.168.1.108'
    MONGODB_PORT = 27018
    MONGODB_DB = 'guba_data'

    def __init__(self):
        try:
            client = MongoClient(self.MONGODB_SERVER, self.MONGODB_PORT)
            self.db = client[self.MONGO_DB]
        except Exception, e:
            print str(e)
            traceback.print_exc()

    @classmethod
    def from_crawler(cls, crawler):
        cls.MONGODB_SERVER = crawler.settings.get('MONGO_SERVER', 'localhost')
        cls.MONGODB_PORT = crawler.settings.get('MONGO_PORT', 27018)
        cls.MONGODB_DB = crawler.settings.get('MONGO_DB', 'guba_data')
        pipe = cls()
        pipe.crawler = crawler
        return pipe

    def process_item(self, item, spider):
        # use stock_num as collection
        post = self.db[item['stock_num']]
        # first get key words, then plus them ,then store
        all_document = post.find_one({'ask_time':item['ask_time']})

        if all_document: # exist ask_time data
            key_words = all_document['key_words']
            # compute every day key words occur times
            key_words = dict_plus(item['key_words'],key_words)
            # find key words, then update
            post.find_one_and_update({'ask_time':item['ask_time'], {'$set':{'key_words':key_words}}})
        else:	# not exist ask_time data
            post.insert({'ask_time':item['ask_time'], 'key_words':item['key_words'})
        return item
