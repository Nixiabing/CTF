# str = [0x55,0x55,0x55,0x55,0x95,0x55,0x5A,0x65,0x55,0x6A,0xA6,0x96,0xAA,0x66,0x66,0x66,0x69,0x55]
# for i in str:
#     print(chr(i))

# str = [97,55,115,104,119,57,111,49,48,101,54,51,110,102,105,49,57,100,107]
# for s in str:
#     print(chr(s),end='')
#
# print('\n')
#
# info = [71,100,24,51,16,97,81,59,53,94,99,100,29,116,25,77,96,27,105]
# for i in info:
#     print(chr(i),end='')
#
# print('\n')
# for i in range(19):
#     info[i] = str[i]^info[i]
#
# for i in range(18):
#     info[i] = info[i] ^ 83
#     info[i] = info[i] ^ info[i+1]
#
# for i in range(1,19):
#     info[i] = info[i] ^ info[i-1]
#
# v40 = info
# v40[0] = 72

# for i in range(1,19):
#     v40 = info[i]^info[i-1]

# glo=[0x66,0x0a,0x6b,0x0c,0x77,0x26,0x4f,0x2e,0x40,0x11,0x78,0x0d,0x5a,0x3b,0x55,0x11,0x70,0x19,0x46,0x1f,0x76,0x22,0x4d,0x23,0x44,0x0e,0x67,0x06,0x68,0x0f,0x47,0x32,0x4f]
# x='f'
# for i in range(1,len(glo)):
#     x+=chr(glo[i]^glo[i-1])
# print(x)

# str = "gnbi|ebubt`goepffadBoacg`upad21n~"
# s = ""
# l = len(str)
# for i in range(l):
#     if i % 2 == 0 :
#         s += chr(ord(str[i]) - 1)
#     else:
#         s += chr(ord(str[i]) - 2)
# print(s)
# l = [97,55,115,104,119,57,111,49,48,101,54,51,110,102,105,49,57,100,107]
# s = [71,100,24,51,16,97,81,59,53,94,99,100,29,116,25,77,96,27,105]
# str = []
# str2 = []
# for i in range(19):
#     str.append(l[i]^s[i])
#
# for i in range(1,19):
#     str[i] ^= str[i - 1]
#
# for i in range(17,-1,-1):
#     str[i] ^= 0x53
#     str[i] ^= s[i + 1]
#
# for i in range(1,19):
#     str[i] ^= str[i - 1]
#
# print(str)

# s = [109,115,104,110,123,108,53,55,105,57,108,49,56,105,48,56,105,109,109,48,107,48,53,104,51,106,53,57,57,48,48,105,49,48,63,63,63,125,116,107,53,58,55,52,50,108,104,56,49,53,50,109,109,49,49,105,49,109,54,109,57,51,49,52,106,51,106,52,108,109,109,57,51,108]
# str = ""
# for i in s:
#     str += chr(i)
# print(str)

# str = "bEBn`GBkMV{fJyMLTF{yR@sQVjUNIoULJVtsN@UQ[d>>"
# string = ""
# for s in str:
#     string += chr(ord(s) ^ 3)
# print(string)

# str_encode = "hP&p0!5L^#3NXLs@*QR%L&UN!L)0%Q^"
# str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+"
# for s in str_encode:
#     num = 0
#     for i in str:
#         if s == i:
#             print(chr(num + 48),end='')
#             break
#         else:
#             num += 1


# str = "kvbsqrd, iye'bo kvwycd drobo! Xyg pyb dro psxkv (kxn wkilo dro rkbnocd...) zkbd: k celcdsdedsyx mszrob. Sx dro pyvvygsxq dohd, S'fo dkuox wi wocckqo kxn bozvkmon ofobi kvzrklodsm mrkbkmdob gsdr k mybboczyxnoxmo dy k nsppoboxd mrkbkmdob - uxygx kc k celcdsdedsyx mszrob. Mkx iye psxn dro psxkv pvkq? rsxd: Go uxyg drkd dro pvkq sc qysxq dy lo yp dro pybwkd edpvkq{...} - grsmr wokxc drkd sp iye coo drkd zkddobx, iye uxyg grkd dro mybboczyxnoxmoc pyb e, d, p, v k, kxn q kbo. Iye mkx zbylklvi gybu yed dro bowksxsxq mrkbkmdobc li bozvkmsxq drow kxn sxpobbsxq mywwyx gybnc sx dro Oxqvscr vkxqekqo. Kxydrob qbokd wodryn sc dy eco pboaeoxmi kxkvicsc: go uxyg drkd 'o' crygc ez wycd ypdox sx dro kvzrklod, cy drkd'c zbylklvi dro wycd mywwyx mrkbkmdob sx dro dohd, pyvvygon li 'd', kxn cy yx. Yxmo iye uxyg k pog mrkbkmdobc, iye mkx sxpob dro bocd yp dro gybnc lkcon yx mywwyx gybnc drkd cryg ez sx dro Oxqvscr vkxqekqo.rghnxsdfysdtghu! qgf isak cthtuike dik zknthhkx rxqldgnxsliq risyykhnk. ikxk tu s cysn cgx syy qgfx isxe kccgxdu: fdcysn{3hrxqld10h_15_r00y}. qgf vtyy cthe disd s ygd gc rxqldgnxsliq tu pfud zftyethn gcc ditu ugxd gc zsutr bhgvykenk, she td xksyyq tu hgd ug zse scdkx syy. iglk qgf khpgqke dik risyykhnk!"
# for s in str:
#     print(chr(ord(s)+11),end="")

# import base64
# file = open("t.txt","r")
# for f in file.readlines():
#     print(base64.b64decode(f))