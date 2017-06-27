#encoding:utf-8
from PIL import Image
import requests
import pytesser
from StringIO import StringIO
import numpy as np
import pandas as pd
import IPython
import sys
import pyocr


image_nums = 200

def get_images():
    url = 'http://175.19.190.18:82/Handler/ValidateCode.ashx?id=2017/4/5%2021:28:41'
    for i in xrange(image_nums):
    # url = 'http://202.119.81.113:8080/verifycode.servlet'
        rep = requests.get(url)
        fp = open('test_images/' + str(i)+'.gif', 'w')
        fp.write(rep.content)
        fp.close()
        print 'get', i, 'picture...'

def binary_diff(img):

    img = img.convert('RGBA')
    pix = img.load()
    color = []

    # for test
    for x in xrange(img.size[0]):
        color.append(reduce(lambda x,y:x+y, pix[x,11][0:3]) / 3)
    # print color
    # raw_input('wait...')
    
    for x in xrange(img.size[0]):
        for y in xrange(img.size[1]):
            if pix[x,y][0] == 255 and (pix[x,y][1] > 0 and pix[x,y][1] < 200) and (pix[x,y][2] >= 0 and pix[x,y][2] <= 100):
                pix[x,y] = (0, 0, 0, 255)
            else:
                    pix[x,y] = (255, 255, 255, 255)
    return img


def handle_images():

    for i in xrange(image_nums):

        image_name = 'test_images/' + str(i) + '.gif'
        im = Image.open(open(image_name, 'r'))
        print im.shape
        raw_input('wait...')
        # print im.size
        img = binary_diff(im)
        pix = img.load()
        # IPython.embed()

        # vertical cut
        vertical_row = [0] * img.size[0]
        for x in xrange(img.size[0]):
            for y in xrange(img.size[1]):
                if pix[x,y][0] == 0:
                    vertical_row[x] += 1
                # print img.getpixel((x,y))
        # print vertical_row
        vertical_cut = []
        pre_sign = False
        pre_not_zero = False
        for i in xrange(img.size[0]):
            if vertical_row[i] >= 3 and pre_sign == False:
                vertical_cut.append(i)
                pre_sign = True
            elif vertical_row[i] < 3 and pre_sign == True:
                vertical_cut.append(i)
                pre_sign = False
        vertical_pic = []
        if len(vertical_cut) == 8:
            for i in xrange(4):
                vertical_pic.append(img.crop((vertical_cut[2*i], 0, vertical_cut[2*i+1], img.size[1]-1)))
            for i in xrange(len(vertical_pic)):
                vertical_pic[i].save(str(i)+'.gif')
        raw_input('wait...')


def another_method():

    url = 'http://175.19.190.18:82/Handler/ValidateCode.ashx?id=2017/4/5%2021:28:41'
    # url = 'http://202.119.81.113:8080/verifycode.servlet'
    rep = requests.get(url)

    im = Image.open(StringIO(requests.get(url).content))
    im.convert('L')
    im_peak = im.convert('1')
    im_peak.show()

    from PIL import ImageFilter,ImageEnhance
    im_filter=im_peak.filter(ImageFilter.MedianFilter)
    for j in range(15):
        im_filter=im_filter.filter(ImageFilter.MedianFilter)
    im_filter.save('test.gif')


if __name__ == '__main__':
    # get_images()
    
    handle_images()
    # while True:
        # another_method()
        # raw_input('wait...')
        # im = get_image()
        # result = crop_picture(im)
