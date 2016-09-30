#!/usr/bin/env python
# encoding: utf-8

import os
import re
import requests
import sys
from bs4 import BeautifulSoup
from lxml import etree
import time
from terminaltables import AsciiTable
import operator
import pickle


def get_data():
    url_raw = 'http://jdjyw.jlu.edu.cn/index.php?r=front/recruit/index&type=1&page=%d'
    data = []

    for page in xrange(1, 21):
        
        table_data = []
        url = url_raw % (page,)
        response = requests.get(url)
        html = etree.HTML(response.content)

        for i in xrange(1, 21):
            info = {}
            line_data = [] 
            company_xpath = '//*[@id="content"]/div/div[2]/div[1]/div[2]/ul/li[%d]/a' % (i,)
            date_address_xpath = '//*[@id="content"]/div/div[2]/div[1]/div[2]/ul/li[%d]/span' % (i,)
            company = html.xpath(company_xpath)
            date_address = html.xpath(date_address_xpath)

            if len(company) == 1 and len(date_address) == 1:
                trans_company = company[0].text.strip()
                line_data.append(trans_company)
                info['company'] = trans_company

                tmp_date_address = date_address[0].text.strip().split()
                raw_date = tmp_date_address[0]
                info['raw_date'] = raw_date
                raw_address = tmp_date_address[1]
                info['address'] = raw_address

                pattern = re.compile(ur'(\d+)月(\d+)日(\d+):(\d+)')
                date_num = pattern.search(raw_date)
                date = int(''.join(date_num.groups()))
                info['date_num'] = date
            else:
                print 'meet error data...'
            data.append(info)


        time.sleep(1)

    sorted_data = sorted(data, key=operator.itemgetter('date_num'))
    pickle_data = pickle.dumps(sorted_data)
    fp = open('data.job', 'w')
    fp.write(pickle_data)
    fp.close()


def read_data():
    f = open('data.job', 'rb')
    sorted_data = pickle.load(f)

    while(True):
        table_data = []
        title_data = ['company', 'time', 'address']
        table_data.append(title_data)

        input_date = raw_input('please enter date:').strip()
        if input_date == '':
            print 'please enter a real date!!'
            continue
        if input_date == 'exit':
            break
        for corp in sorted_data:
            tmp_data = []
            str_date = str(corp['date_num'])
            if input_date in str_date:
                company = corp['company'].strip()
                if len(company) > 35:
                    tmp_data.append(company[:35])
                else:
                    tmp_data.append(company)
                tmp_data.append(corp['raw_date'])
                tmp_data.append(corp['address'])
                table_data.append(tmp_data)

        table = AsciiTable(table_data)
        print table.table
        print "total: ", len(table_data)


if __name__ == '__main__':
    os.system('clear')

    get_data()

    read_data()
