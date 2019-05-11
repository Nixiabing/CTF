# import base64
# str = "e6Z9i~]8R~U~QHE{RnY{QXg~QnQ{^XVlRXlp^XI5Q6Q6SKY8jUAA"
# data = ""
# for i in range(len(str)):
#     data += chr(ord(str[i])-4)
# print(base64.b64decode(data))
# str = "gndk€rlqhmtkwwp}z"
# data = ""
# for i in range(len(str)):
#     data += chr(ord(str[i]) - 1 -i)
# print(data)
# q = ""
# s = [87,0x65,0x6c,0x63,0o157,109,0o145,0b100000,116,0b1101111,0o40,0x6b,0b1100101,0b1101100,0o141,105,0x62,101,0b1101001,46,0o40,71,0x69,118,0x65,0x20,0b1111001,0o157,0b1110101,32,0o141,32,102,0o154,0x61,0x67,0b100000,0o141,115,0b100000,0b1100001,32,0x67,0o151,0x66,116,0b101110,0b100000,32,102,108,97,0o147,123,0x31,0b1100101,0b110100,98,102,0b111000,49,0b1100001,54,0b110011,0x39,0o64,0o144,0o145,53,0x61,0b1100010,0b1100011,0o60,48,0o65,0b1100001,0x63,0b110110,101,0o63,0b111001,97,51,0o70,55,0b1100010,125,0x20,0b101110,0x20,0b1001000,97,118,0o145,0x20,97,0o40,103,111,111,0x64,32,0o164,0b1101001,0x6d,0o145,0x7e]
# for i in range(len(s)):
#     q += chr(s[i])
# print(q)
# -*- coding: utf-8 -*-
def round_add(a, b):
    f = lambda x, y: x + y - 2 * (x & y)
    res = ''
    for i in range(len(a)):
        res += chr(f(ord(a[i]), ord(b[i])))
    return res


def permutate(table, block):
    return list(map(lambda x: block[x], table))


def string_to_bits(data):
    data = [ord(c) for c in data]
    l = len(data) * 8
    result = [0] * l
    pos = 0
    for ch in data:
        for i in range(0, 8):
            result[(pos << 3) + i] = (ch >> i) & 1
        pos += 1
    return result


s_box = [54, 132, 138, 83, 16, 73, 187, 84, 146, 30, 95, 21, 148, 63, 65, 189, 188, 151, 72, 161, 116, 63, 161, 91, 37,
         24, 126, 107, 87, 30, 117, 185, 98, 90, 0, 42, 140, 70, 86, 0, 42, 150, 54, 22, 144, 153, 36, 90, 149, 54, 156,
         8, 59, 40, 110, 56, 1, 84, 103, 22, 65, 17, 190, 41, 99, 151, 119, 124, 68, 17, 166, 125, 95, 65, 105, 133, 49,
         19, 138, 29, 110, 7, 81, 134, 70, 87, 180, 78, 175, 108, 26, 121, 74, 29, 68, 162, 142, 177, 143, 86, 129, 101,
         117, 41, 57, 34, 177, 103, 61, 135, 191, 74, 69, 147, 90, 49, 135, 124, 106, 19, 89, 38, 21, 41, 17, 155, 83,
         38, 159, 179, 19, 157, 68, 105, 151, 166, 171, 122, 179, 114, 52, 183, 89, 107, 113, 65, 161, 141, 18, 121, 95,
         4, 95, 101, 81, 156, 17, 190, 38, 84, 9, 171, 180, 59, 45, 15, 34, 89, 75, 164, 190, 140, 6, 41, 188, 77, 165,
         105, 5, 107, 31, 183, 107, 141, 66, 63, 10, 9, 125, 50, 2, 153, 156, 162, 186, 76, 158, 153, 117, 9, 77, 156,
         11, 145, 12, 169, 52, 57, 161, 7, 158, 110, 191, 43, 82, 186, 49, 102, 166, 31, 41, 5, 189, 27]


def generate(o):
    k = permutate(s_box, o)
    b = []
    for i in range(0, len(k), 7):
        b.append(k[i:i + 7] + [1])
    c = []
    for i in range(32):
        pos = 0
        x = 0
        for j in b[i]:
            x += (j << pos)
            pos += 1
        c.append((0x10001 ** x) % (0x7f))
    return c


class N1ES:
    def __init__(self, key):
        if (len(key) != 24 or isinstance(key, bytes) == False):
            raise Exception("key must be 24 bytes long")
        self.key = key
        self.gen_subkey()

    def gen_subkey(self):
        o = string_to_bits(self.key)
        k = []
        for i in range(8):
            o = generate(o)
            k.extend(o)
            o = string_to_bits([chr(c) for c in o[0:24]])
        self.Kn = []
        for i in range(32):
            self.Kn.append(map(chr, k[i * 8: i * 8 + 8]))
        return

    def encrypt(self, plaintext):
        if (len(plaintext) % 16 != 0 or isinstance(plaintext, bytes) == False):
            raise Exception("plaintext must be a multiple of 16 in length")
        res = ''
        for i in range(len(plaintext)/16):
            block = plaintext[i * 16:(i + 1) * 16]
            L = block[:8]
            R = block[8:]
            for round_cnt in range(32):
                L, R = R, (round_add(L, self.Kn[round_cnt]))
            L, R = R, L
            res += L + R
        return res


print(N1ES(('wxy191iss00000000000cute')))


