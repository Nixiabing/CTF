from PIL import Image
image = Image.open("xs.png")
img = image.load()
for y in range(0,100):
    for x in range(0, 10):
        #print(img[x, y])
        if(str(img[x,y]) != "(255, 0, 0)"):
            print(img[x, y])
        # if((str(img[x,y]) != "(156, 254, 239)") and (img[x,y]) != "(155, 255, 240)"):
        #      print(img[x,y])
aq = [
100,
50,
98,
51,
48,
50,
56,
99,
100,
53,
102,
56,
55,
97,
53,
48,
]
# aq = [
# 56,
# 99,
# 100,
# 53,
# 100,
# 102,
# 50,
# 56,
# 98,
# 55,
# 51,
# 97,
# 48,
# 53,
# 50,
# 48,
# ]
s=""
for a in aq:
    s += (chr(a))
print(s)