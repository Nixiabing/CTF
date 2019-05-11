import base64

for line in open("123.txt"):
    line = base64.b64decode(line)
    print(line)