import urllib.parse
print(urllib.parse.quote(open("shattered-2.pdf", "rb").read()[:320]))# url编码
#print(open("shattered-1.pdf", "rb").read()[:320])