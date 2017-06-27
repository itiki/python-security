#encoding:utf-8

from wxpy import *
import requests
import json
from threading import Timer
from datetime import datetime
import schedule
import time
import urllib  
import json  


bot = Bot(cache_path=True, console_qr=2)
key = '8b005db5f57556fb96dfd98fbccfab84'  
tuling = Tuling(api_key=key)

try:
    xina1i = bot.friends().search('xina1i')[0]
    ymny = bot.friends().search('YMNY')[0]
except Exception as e:
    # print(e)
    pass

           
@bot.register(ymny)
def reply_ymny(msg):
    tuling.do_reply(msg)


@bot.register(xina1i)
def reply_xina1i(msg):
    if u'图:' in msg.text:
        msg.text = msg.text.split(':')[1]
        tuling.do_reply(msg)


def parse_weather(data):
    cloud = '风与云彩: ' + data['fengxiang']+' '+data['fengli']+' '+data['type']
    temperature = '气温: ' + data['low'].split()[1] + '-' + data['high'].split()[1]
    return cloud+'\n'+temperature + '\n'


def get_weather():
    error_sign = False
    weather_url = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101060201'

    try:
        # weather_caution = u'小涛哥哥专为小茜姐姐设置的机器人提醒今日天气状况:\n'
        weather_caution = u'今日天气状况:\n'

        r = requests.get(weather_url)
        weather_data = json.loads(r.text)
        today = weather_data['data']['forecast'][0]
        today_data = parse_weather(today)
        suggestion = '感冒指数: ' + weather_data['data']['ganmao']
        current_temperature = '\n当前温度: ' + weather_data['data']['wendu']
        return weather_caution + today_data + suggestion + current_temperature
    except Exception as err:
        error_sign = True


def send_weather():
    weather = get_weather()
    # if xina1i:
    if ymny:
        ymny.send(weather)
    # bot.core.send(weather, toUserName='filehelper')
        print('send message successfully')
    else:
        print('No friend')
        

def test_logger():
    pass
    # logger = get_wechat_logger()
    # logger.warning('this is a warings message')

def main():

    # schedule.every().minutes.do(gift.send_gift)
    schedule.every().day.at("07:00").do(send_weather)
    # schedule.every().minutes.do(send_weather)
    while True:
        schedule.run_pending()
        # test_logger()
        time.sleep(10)


if __name__ == '__main__':
    main()
