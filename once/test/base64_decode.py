import base64
# f = open("bin.txt",'r')
# by = base64.b64decode(f.read())
# file = open("zip.zip","wb")
# file.write(by)


f = "H4sICE5ZSl0CAGZsYWcudGFyAO3RwQmAMAyF4YzSBQpJTEg6TivWixuIu2sPggv0IvkuD97170fdYTJCNLMEacDPvpQTLcosKoryHGLGCRDCbKP/WbhS41ay8epZ1Fqu3NfsKoJbdxcqF4QQQviRG6tR4ssACAAA"
de = base64.b64decode(f)
file = open("flag.rar","wb")
file.write(de)