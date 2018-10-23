import base64

for line in open("crypto_string.txt"):
    for i in range(40):
        line = base64.b64decode(line)
        print(line)