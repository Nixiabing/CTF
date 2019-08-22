import base64
str = "AAoHAR1XICMnIlBfUlRXXyBXJFRSUCRRI1RSJyQkIlYgU1EjURs="
s = (base64.b64decode(str)).decode()

for i in range(256):
    print(i)
    for n in s:
        print(chr(ord(n)^i),end='')
    print('')