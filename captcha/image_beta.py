from PIL import Image
import requests
import pytesser
from StringIO import StringIO
import numpy as np
import pandas as pd
import IPython
import sys
import pyocr


def rgb(im):
    width, heigth = im.size
    data = np.zeros((heigth,width))
    aa = []
    for w in range(width):
        for h in range(heigth):
            y=im.getpixel((w,h)) 
            data[h,w] = y
            aa.append(y)

    data = pd.DataFrame(data)
    aa = pd.Series(aa)
    return aa,data

def topliangdu(liangdu, biaozhun=100):

    c = liangdu.value_counts()
    return list(c[c>100].index)


def liangdutianbai(im, mubiao):
    width, heigth = im.size
    for w in range(width):
        for h in range(heigth):
            y = im.getpixel((w,h))
            if y not in mubiao:
                im.putpixel([w,h], (255,255,255))
    return im


def tongse(im):

    global aa, data
    aa,data = rgb(im)
    mubiao = topliangdu(aa)
    im = liangdutianbai(im, mubiao)
    img_grey = im.convert('L')
    img_grey.show()
    return img_grey


def get_image():
    url = 'http://175.19.190.18:82/Handler/ValidateCode.ashx?id=2017/4/5%2021:28:41'
    # url = 'http://202.119.81.113:8080/verifycode.servlet'
    rep = requests.get(url)

    im = Image.open(StringIO(requests.get(url).content))
    im = im.convert('RGBA')
    im.show()
    pix = im.load()
    
    for x in xrange(im.size[0]):
        for y in xrange(im.size[1]):
            if pix[x,y][0] == 255 and (pix[x,y][1] > 0 and pix[x,y][1] < 200) and (pix[x,y][2] >= 0 and pix[x,y][2] <= 100):
                pix[x,y] = (0, 0, 0, 255)
            else:
                pix[x,y] = (255, 255, 255, 255)
    im.save('tmp.gif')
    im.show()
    
    # tools = pyocr.get_available_tools()
    # if len(tools) == 0:
        # print "No OCR tool found"
        # sys.exit(1)
    # The tools are returned in the recommended order of usage
    # tool = tools[0]

    # digits = tool.image_to_string(Image.open('tmp.gif'))
    txt = pytesser.image_to_string('tmp.gif')
    print digits
    print txt
    raw_input('wait...')



if __name__ == '__main__':
    # main()
    while True:
        get_image()
