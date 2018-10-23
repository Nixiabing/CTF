import requests
import base64

cookies = {
    'PHPSESSID': 'vjv0qlg0g82kue4tcb09d1dvvc68tko9',
}

headers = {
    'Host': '123.206.87.240:8002',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://ctf.bugku.com/challenges',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}


url = 'http://123.206.87.240:8002/web6/'
response = requests.session()
response1 = response.get(url,headers=headers,cookies=cookies)
re = (base64.b64decode(response1.headers['flag']).decode()).split(":")[1]
data = { 'margin' : base64.b64decode(re).decode() }
response2 = response.post(url,data=data,headers=headers,cookies=cookies)
print(response2.text)