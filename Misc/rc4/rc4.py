# str = [0o111,0o114,0o157,0o166,0o145,0o123,0o145,0o143,0o165,0o162,0o151,0o164,0o171,0o126,0o145,0o162,0o171,0o115,0o165,0o143,0o150]
# for i in str:
#     print(chr(i),end='')
# key = "whoami"
# flag = "????????????????????????????????"
# s = [0 for i in range(257)]
# t = [0] * 257
# j = 0
# for i in range(257):
#     t[i] = key[i % 5]
# for i in range(257):
#     j = (j + s[i] + t[i]) % 256
#     s[i] = s[j]
# i = 0
# j = 0
# for m in range(39):
#     i = (i + 1) % 256
#     j = (j + s[i]) % 256
#     s[i] = s[j]
#     x = (s[i] + (s[j] % 256)) % 256
#     flag[m] = flag[m] ^ s[x]
f = open("file.txt","rb")
c = f.read()

flagx = [0x00,0xba,0x8f,0x11,0x2b,0x22,0x9f,0x51,0xa1,0x2f,0xab,0xb7,0x4b,0xd7,0x3f,0xef,0xe1,0xb5,0x13,0xbe,0xc4,0xd4,0x5d,0x03,0xd9,0x00,0x7a,0xca,0x1d,0x51,0xa4,0x73,0xb5,0xef,0x3d,0x9b ,0x31,0xb3]
key = "whoami"
print(len(key))
s = list(range(256))
t = [0] * 257
j = 0

for i in range(256):
    j = (j + s[i] + ord(key[i % 6])) % 256
    s[i],s[j] = s[j],s[i]
i = 0
j = 0
for r in c:
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    s[i],s[j] = s[j],s[i]
    x = (s[i] + (s[j] % 256)) % 256
    print(chr(s[x]^r),end='')

# key = 'whoami'
# ch = ''
# j = 0 #初始化
# s = list(range(256)) #创建有序列表
# for i in range(256):
#     j = (j + s[i] + ord(key[i % len(key)])) % 256
#     s[i],s[j] = s[j],s[i]
# i = 0 #初始化
# j = 0 #初始化
# for r in c:
#     i = (i + 1)  % 256
#     j = (j + s[i])  % 256
#     s[i], s[j] = s[j], s[i]
#     x = (s[i] + (s[j] % 256)) % 256
#     ch += chr(r ^ s[x])
# print(ch)