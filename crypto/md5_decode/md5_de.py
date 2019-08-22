import hashlib
import string

strings = string.printable
str = []
for i in strings:
            sum = i
            str.append(sum)

for s in str:
    md = s
    for i in range(10):
        md = hashlib.md5(md.encode()).hexdigest().upper()
    print(s + " : " + md)