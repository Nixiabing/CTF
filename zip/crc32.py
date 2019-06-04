# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import requests

header = {'Cookie': 'PHPSESSID=3bc379e81461e47b269e44f5a06b6bbe'}

def vcode():
    "python验证码识别函数"
    pic_url = 'http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/vcode.php'
    r = requests.get(pic_url, headers=header, timeout=10)
    with open('vcode.png', 'wb') as pic:
        pic.write(r.content)
    im = pytesseract.image_to_string(Image.open('vcode.png'))
    im = im.replace(' ', '')
    if im != '':
        print(im)
    else:
        return vcode()
im = pytesseract.image_to_string(Image.open('111.png'))
im = im.replace(' ', '')
if im != '':
    print(im)