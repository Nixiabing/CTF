import base64
f = open("bin.txt",'r')
by = base64.b64decode(f.read())
file = open("zip.zip","wb")
file.write(by)