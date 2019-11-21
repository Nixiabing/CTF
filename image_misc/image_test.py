from PIL import Image
import binascii

img = Image.open("solved.bmp")
img_array = img.load()
print(img.size) # 查看图像尺寸
# img_array[x,y]) #查看像素点


# img1 = Image.open("45.bmp")
# img_array1 = img1.load()
# img2 = Image.open("45_1.bmp")
# img_array2 = img2.load()

sum = ""
for x in range(3):
    for y in range(220):
        print(x,",",y," : ",img_array[x,y])
        # if img_array[x,y] == img_array2[x,y]:
        #     sum += "0"
        # else:
        #     sum += "1"

print(sum)