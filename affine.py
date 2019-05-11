from pycipher import Affine
encode = Affine(a=5,b=9).encipher('defend the east wall of the castle')
print("加密结果：" + encode)
decode =Affine(a=5,b=12).decipher('RgYDMllaKzGC')
print("解密结果：" + decode)
# 注意大小写