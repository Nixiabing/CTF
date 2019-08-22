# import base64
#
# s = b''
# sum = b''
#
# with open("out.txt","r") as File:
#     file = File.readlines()
#     for f1 in file:
#         if f1[0:9] == '$$START$$' and f1 != s:
#             #print(i[9:].decode(),end='')
#             meta = base64.b64decode(f1[9:])
#             sum += meta
#             s = f1
#
# f2 = open("test.zip","wb")
# f2.write(sum)

str = "011011010100010000110101010111110011000101110100"
i = 0
while i < len(str):
    s = int(str[i:i+8],2)
    print(chr(s),end='')
    i += 8
