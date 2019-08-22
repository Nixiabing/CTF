#! python3
# -*- coding: utf-8 -*-
# @Time    : 2017/8/26 上午12:07
# @Author  : BlingBling
# @File    : Baconian.py
# @Software: PyCharm Community Edition
import re
class Baconian():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    first_cipher = ["aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba", "aabbb", "abaaa", "abaab", "ababa",
                    "ababb", "abbaa", "abbab", "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb", "babaa", "babab",
                    "babba", "babbb", "bbaaa", "bbaab"]

    second_cipher = ["aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba", "aabbb", "abaaa", "abaaa", "abaab",
                     "ababa", "ababb", "abbaa", "abbab", "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb", "baabb",
                     "babaa", "babab", "babba", "babbb"]

    def __init__(self, str):
        self.str = str

    def decode(self):
        str = self.str.lower()
        str_array = re.findall(".{5}", str)
        decode_str1 = ""
        decode_str2 = ""
        for key in str_array:
            for i in range(0,26):
                if key == Baconian.first_cipher[i]:
                    decode_str1 += Baconian.alphabet[i]
                if key == Baconian.second_cipher[i]:
                    decode_str2 += Baconian.alphabet[i]

        print(decode_str1)
        print(decode_str2)



if __name__ == '__main__':
    str = input("please input string to decode:\n")
    bacon = Baconian(str)
    bacon.decode()