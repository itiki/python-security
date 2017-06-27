#encoding:utf-8

import os
import requests
from datetime import datetime



def book():

    """time_code
    {code:"D",t_info:"07:00-08:00" },{code:"E",t_info:"08:00-09:00" },{code:"1",t_info:"09:00-10:00" },{code:"2",t_info:"10:00-11:00" },{code:"3",t_info:"" },{code:"4",t_info:"11:00-12:00" },{code:"F",t_info:"12:00-13:00" },{code:"5",t_info:"13:00-14:00" },{code:"6",t_info:"14:00-15:00" },{code:"7",t_info:"15:00-16:00" },{code:"8",t_info:"16:00-17:00" },{code:"G",t_info:"17:00-18:00" },{code:"9",t_info:"18:00-19:00" }
   """
    time_code = {}
    weekday_chinese = {
            '0': u'一',
            '1': u'二',
            '2': u'三',
            '3': u'四',
            '4': u'五',
            '5': u'六',
            '6': u'日'}

    headers = {
            'Cookie':'ASP.NET_SessionId=eogwfbevnqtvcn45lqyyns45'
        }
    url = 'http://175.19.190.18:82/Student/Index.aspx?t=0.0959681990264254&style=0'
    url = 'http://175.19.190.18:82/wsyy/stu_yueche.aspx?codeid=ODgxMQ=='

    # yyyy-mm-dd(weekday)$time_code,|
    # such as '2017-04-05(三)$E,|' ==> choose 08:00-09:00
    date_str = raw_input('Input Date(yyyy-mm-dd): ')
    time_zone = raw_input()

    date = datetime.strptime(date, '%Y-%M-%D')
    weekday = weekday_chinese[datetime.weekday(date)]
    yueMsgs = date + '(' + weekday + ')'

    url = 'http://175.19.190.18:82/Handler/wsyy/SaveYueHandler.ashx?_=1491376522253&yueMsgs=MjAxNy0wNC0xMCjkuIApJDUsfA%3D%3D&codeid=ODgxMQ%3D%3D&jlName=5byg5pmT6Ziz&jlid=8811&jlMobile=15304486696&carst=%3CPXLX002%3E&dcdd='
    req = requests.get(url, headers=headers)
    print req.text

    req = requests.get(url, headers=headers)
    print req.text


def main():
    book()


if __name__ == '__main__':
    main()
