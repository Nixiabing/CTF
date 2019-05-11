#!/usr/bin/python

with open("flag.png","rb") as f:
    tmp = f.read()

with open("flag2.png","wb") as f:
    f.write(tmp[::-1])