# str = [0x55,0x55,0x55,0x55,0x95,0x55,0x5A,0x65,0x55,0x6A,0xA6,0x96,0xAA,0x66,0x66,0x66,0x69,0x55]
# for i in str:
#     print(chr(i))

str = [97,55,115,104,119,57,111,49,48,101,54,51,110,102,105,49,57,100,107]
for s in str:
    print(chr(s),end='')

print('\n')

info = [71,100,24,51,16,97,81,59,53,94,99,100,29,116,25,77,96,27,105]
for i in info:
    print(chr(i),end='')

print('\n')
for i in range(19):
    info[i] = str[i]^info[i]

for i in range(18):
    info[i] = info[i] ^ 83
    info[i] = info[i] ^ info[i+1]

for i in range(1,19):
    info[i] = info[i] ^ info[i-1]

v40 = info
v40[0] = 72
# for i in range(1,19):
#     v40 = info[i]^info[i-1]