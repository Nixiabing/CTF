# str = "10100010001010100110001000100010001000100010011000101010001000101010001010101010101000100010101000101010001000101010011010101010"
# for i in range(len(str)):
#     if i % 8 == 0:
#         m = str[i:i+8]
#         s = hex(int(m,2))
#         print(s,end='')

# str = "afZ_r9VYfScOeO_UL^RWUc"
# s = 5
#
# for i in str:
#     m = chr(ord(i) + s)
#     s += 1
#     print(m,end='')

import hashlib
for i in range(32,127):
    for j in range(32,127):
        for k in range(32,127):
            m=hashlib.md5()
            m.update('TASC'+chr(i)+'O3RJMV'+chr(j)+'WDJKX'+chr(k)+'ZM')
            des=m.hexdigest()
            if 'e9032' in des and 'da' in des and '911513' in des:
                print(des)