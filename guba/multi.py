#!/usr/bin/env python
# encoding: utf-8

import multiprocessing
import os
from pymongo import MongoClient
from redis import Redis
import re
import time

from clear import drop_mongo


MONGO_SERVER = '192.168.1.108'
MONGO_PORT_IN = 27017
MONGO_DB_IN = 'guba_data'
MONGO_DB_OUT = 'guba'
MONGO_PORT_OUT = 27018
REDIS_SERVER = '192.168.1.108'
REDIS_PORT = 6379

process_nums = multiprocessing.cpu_count()
redis_client = Redis(REDIS_SERVER, REDIS_PORT)
mongo_client_in =  MongoClient(MONGO_SERVER, MONGO_PORT_IN)
mongo_client_out =  MongoClient(MONGO_SERVER, MONGO_PORT_OUT)
mongo_db_in = mongo_client_in[MONGO_DB_IN]
mongo_db_out = mongo_client_out[MONGO_DB_OUT]
# strip, then unicode, then compile
key_words = [ re.compile(unicode(key.strip(), 'utf-8')) for key in open('keywords.txt', 'r').readlines() ]


def add(x, y):
    return x + y

def store2mongo(stock_num, ask_time, key_words_accouts):
    post = mongo_db_out[stock_num]
    # first get key words, then plus them ,then store
    all_document = post.find_one({'ask_time':ask_time})
    # exist ask_time data
    if all_document:
        key_words_accouts_before = all_document['key_words']
        post_times = all_document['post_times']
        # compute every day key words occur times
        key_words_accouts_after = map(add, key_words_accouts, key_words_accouts_before)
        # find key words, then update
        post.update_one({'ask_time':ask_time}, {'$set':{'key_words':key_words_accouts_after, \
                'post_times':post_times+1}})
    else:    # not exist ask_time data
        post.insert({'ask_time':ask_time, 'post_times':1, 'key_words':key_words_accouts})
    print stock_num, ask_time

def handle_data(stock_num):
    # stock num represent a collection
    # print 'test'
    table = mongo_db_in[stock_num]
    if table and table.count() > 0:
        for post_day in table.find():
            # get post ask time
            ask_time = post_day['ask_time']
            # store key words occur times
            key_words_accouts = []
            # this day present occur 1 time
            replys_data = post_day['replys_data']

            for pattern in key_words:
                # initial find_count is 0
                key_find_count = 0
                for text in replys_data:
                    result = pattern.findall(text)
                    if result:
                        key_find_count = len(result)
                key_words_accouts.append(key_find_count)
            store2mongo(stock_num, ask_time, key_words_accouts)

def handle(process_name):
    print process_name, 'is running...'
    while redis_client.scard('stocks') > 0:
        # use a set to store stock nums
        stock_num = redis_client.spop('stocks')
        if stock_num:
            stock_num = 'db' + stock_num
            handle_data(stock_num)
            # print 'here'

def main():
    pools = multiprocessing.Pool()
    for i in xrange(process_nums - 1):
        process_name = 'process_' + str(i)
        pools.apply_async(handle, (process_name, ))
    pools.close()
    pools.join()
    print 'all process done.....'

if __name__ == '__main__':
    os.system('printf "\033c"')

    start = time.time()
    main()
    end = time.time()
    print 'used time: ', (end - start) / 60.0
