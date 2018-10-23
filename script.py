#!/usr/bin/env python
# coding:utf-8
import base64

def encrypto(string):
    str1 = ""
    for i in string:
        str1 += chr((ord(i) + 8) ^ 0x16)
    str2 = ""
    for j in base64.b16encode(str1):
        str2 += chr(ord(j) ^ 0x32)
    str3 = ""
    for k in base64.b32encode(str2):
        str3 += chr(ord(k) ^ 0x64)
    return base64.b64encode(str3)

def decrypty(string):
    # decrypto code .....
    s1 = s2 = s3 = ""
    for k in base64.b64decode(string):
        s3 += chr(ord(k)^0x64)
    for j in base64.b32decode(s3):
        s2 += chr(ord(j)^0x32)
    for i in base64.b16decode(s2):
        s1 += chr((ord(i)^0x16)-8)
    return s1

def main():
    string = "123456"
    encrypto_str = "JTEiJS0lJSIrNSc1Myc9LCUyPjUlUCUiKyUlLCsmKDAlMlYlL1ElIiYtJSwnJSA1JVAnNS9QLSUrJSUsJSYoMSUmVyUlUTUlJiklJTMmKDMlJlclJVA9JSslJSwnJj0hJSZXJS9RJSUrJSUsLSY9ISUmPTUrJiUoJSFZWVlZWVk="
    print encrypto(string)
    print decrypty(encrypto_str)

if __name__ == "__main__":
    main()