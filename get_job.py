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
import IPython
import datetime

from sendmail import sendmail

data_path = '/home/xinali/python/'

def get_data():
    site = 'http://jdjyw.jlu.edu.cn'
    url_raw = 'http://jdjyw.jlu.edu.cn/index.php?r=front/recruit/index&type=1&page=%d'
    data = []

    for page in range(1, 21):
        
        table_data = []
        url = url_raw % (page,)
        # print ('getting page %d...' % page)
        response = requests.get(url)
        html = etree.HTML(response.content)

        for i in range(1, 21):
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
                info['company_href'] = '<a href="%s%s">前往</a>' % (site, company[0].get('href'))

                tmp_date_address = date_address[0].text.strip().split()
                if len(tmp_date_address) == 1:
                    break
                raw_date = tmp_date_address[0]
                info['raw_date'] = raw_date
                raw_address = tmp_date_address[1]
                info['address'] = raw_address

                pattern = re.compile(r'(\d+)月(\d+)日(\d+):(\d+)')
                date_num = pattern.search(raw_date)
                month_day = date_num.group(1) + date_num.group(2)
                # IPython.embed()
                # input('wait...')
                date = int(''.join(date_num.groups()))
                info['date_num'] = date
                info['month_day'] = month_day
            else:
                print ('meet error data...')
            data.append(info)

        time.sleep(1)

    sorted_data = sorted(data, key=operator.itemgetter('date_num'))
    pickle_data = pickle.dumps(sorted_data)
    fp = open(data_path + 'data.job', 'wb')
    fp.write(pickle_data)
    fp.close()

def trans_date(x):
    if len(x) == 1:
        return '0' + x
    else:
        return x

def read_data():

    f = open(data_path + 'data.job', 'rb')
    sorted_data = pickle.load(f)

    table_data = []
    title_data = ['公司名称', '宣讲会时间', '宣讲会地点', '就业网地址']
    table_data.append(title_data)
    today = datetime.datetime.today()
    # f = lambda x: len(x) == 1 ? '0' + x : 
    input_date = trans_date(str(today.month)) + trans_date(str(today.day))
    # print (input_date)
    # input('wait...')

    # while True:
        # input_date = input('date:')
    print (input_date)
    for corp in sorted_data:
        tmp_data = []
        # str_date = str(corp['date_num'])
        str_date = corp['month_day']
        # print (str_date)
        # input('wait...')
        if input_date == str_date:
            company = corp['company'].strip()
            if len(company) > 35:
                tmp_data.append(company[:35])
            else:
                tmp_data.append(company)
            tmp_data.append(corp['raw_date'])
            tmp_data.append(corp['address'])
            tmp_data.append(corp['company_href'])
            table_data.append(tmp_data)

    msg_content = """<html><body>
    <table>%s</table></body></html>"""
    content = ''

    for table in table_data:
        content += '<tr>'
        for row in table:
            content += '<td>' + row + '</td>\n'
        content += '</tr>'
    msg_content = msg_content % content
        # print (msg_content)
        # input('wait...')
    # print msg_content
    # to_addrs = []
    to_addrs = ['daitaomail@gmail.com', '876247994@qq.com', '764668301@qq.com', '893142912@qq.com', '1617479714@qq.com', '383852346@qq.com', '727258362@qq.com', '2686792916@qq.com', '1494838847@qq.com']
    # to_addrs = ['1494838847@qq.com']
    # subject = '2016年%d月%d日宣讲会信息(修正版)' % (today.month, today.day)
    subject = '2016年%d月%d日宣讲会信息' % (today.month, today.day)
    msg_type = 'html'
    to_addrs.append('1447932441@qq.com')
    for to_addr in to_addrs:
        sendmail(to_addr, subject, msg_content, msg_type)
        # time.sleep(60)


if __name__ == '__main__':
    os.system('clear')

    get_data()
    read_data()
