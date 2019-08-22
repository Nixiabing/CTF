# -*- coding:utf-8 -*-
a =open('1.txt','rb').read()
b =open('2.txt','rb').read()
lut = ' '
for i in range(32):
    print(chr(a[i]^b[i]),end='')