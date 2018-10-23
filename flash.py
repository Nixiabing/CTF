import requests

cookies = {
    'PHPSESSID': 'gdoagmlhklpc53q797nsl2g3g2',
    'csrf_token': 'loJd4OYqPj1OKhlYgcD3',
}

headers = {
    'Host': 'h3.l1n3.net:20180',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://h3.l1n3.net:20180/web06_8f0a/index.php?num=12',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}

params = (
    ('num', '11'),
)

for i in range(100):
    response = requests.get('http://h3.l1n3.net:20180/web06_8f0a/index.php', headers=headers, params=params, cookies=cookies)
    html = response.text
    s = html.find('<!DOCTYPE html>')
    if(html[0:s] != 11):
        continue
    else:
        print(html)
        break


