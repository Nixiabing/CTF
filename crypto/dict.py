# 数组随机排列
import itertools
import string

# str = ["%","1","D","w","3","s","2","."]
str = string.printable

nums = itertools.permutations(str)

for x in  nums:
    for i in x:
        print(i,end='')
    print("")