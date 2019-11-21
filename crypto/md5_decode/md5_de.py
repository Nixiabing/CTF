import hashlib
import string

# strings = string.printable
# str = ""
# for j in range(3):
#     for i in strings:
#         str += i

f = open("sup.txt","r")
for i in f.readlines():
    de_str = "flag{" + "e57b9e18b08bff0d05a3c59900b10{}".format(i.replace("\n", "")) + "}"
    md = hashlib.md5(de_str.encode()).hexdigest().lower()
    if md == "742ea8152ff11b1f6f9314c3c4eff93e":
        print(de_str)
# for s in str:
#     md = s
#     for i in range(10):
#         md = hashlib.md5(md.encode()).hexdigest().upper()
#     print(s + " : " + md)