# W型加密

string = input("输入要加密的字符串\n")

length = len(string)

# 猜想不会是一栏,和n栏（滑稽）因为这个就是原来字符串（狗头）

# 那么，就暴力遍历一波其中的那些⑧

for i in range(2, length):

    result = {x: "" for x in range(i)}

    for a in range(length):

        width = i * 2 - 2

        num = a % width

        if (num < i):
            result.update({num: result[num] + string[a]})

        else:

            ll = 2 * i - 2 - num
            result.update({ll: result[ll] + string[a]})

    d = ''

    for k in range(i):
        d = d + result[k]
    print("分为" + str(i) + "栏,结果是：" + d)