
key_file = open("key.txt","r")
mi_file = open("mi.txt","r")
# for k in key_file.read():
#     print(k,end='')
#     for m in mi_file.read():
#         print(m)
        # print(chr(ord(k)^ord(m)),end='')
text = ""
k = key_file.read()
m = mi_file.read()
for i in range(38):
    text += chr(ord(k[i])^ord(m[i]))
print(text)