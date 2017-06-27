#!/usr/bin/env python
# encoding: utf-8

import os
from pymongo import MongoClient

def show():
    server = MongoClient()
    db = server.guba
    for stocknum in open('stocknums.txt', 'r'):
        collec = 'db' + stocknum.strip()
        collection = db[collec]
        if collection.count() > 700:
            print stocknum.strip(), collection.count()

if __name__ == '__main__':
    os.system('printf "\033c"')

    show()
