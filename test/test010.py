#
# file = open("Welcome.txt","r")
# s = file.readline().split(" ")
# for i in s:
#     print(i)

# 16进制数转字符
# str = "666c61677b495343435f57454c434f4d457d"
# flag = ""
# for i in range(0,len(str),2):
#     flag += chr(int(str[i:i+2],16))
# print(flag)

# base64写入png
# import base64
# a=open('1.txt','rb').read()
# d=base64.b64decode(a)
# filename='2.png'
# with open(filename,'w') as file_project:
#     file_project.write(d)
import HTMLParser

s = 'flag{PrEtTy_1ScC9012_gO0d}'
h = HTMLParser.HTMLParser()
print(h.unescape(s))