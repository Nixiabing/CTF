import requests

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

response = requests.session()

response1 = response.get('http://123.206.87.240:8002/qiumingshan/', headers=headers, cookies=cookies)
html = response1.text
a1 = html.find("<div>")
a2 = html.find("=?")
num = html[ a1+5 : a2 ]
data = {'value' : eval(num)}
print(num)
response2 = response.post('http://123.206.87.240:8002/qiumingshan/',data=data, headers=headers, cookies=cookies)
print(response2.text)



