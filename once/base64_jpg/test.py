# import base64
#
# s = b''
# for line in open("fenxi.php"):
#     s += base64.b64decode(line)
# file = open("123.jpg","wb+")
# file.write(s)

# a = [102,108,97,103,123,52,55,101,100,98,56,51,48,48,101,100,53,102,57,98,50,56,102,99,53,52,98,48,100,48,57,101,99,100,101,102,55,125]
a = [107,111,101,107,106,51,115]
for i in a:
    print(chr(i),end="")