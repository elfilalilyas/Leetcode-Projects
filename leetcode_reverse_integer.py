def reverseInteger(x):
    num = abs(x)
    if num < 10:
        return x
    str_num = 0
    while True:
        rest = num % 10
        str_num = str_num * 10 + rest
        num = num // 10
        if num // 10 == 0:
            str_num = str_num*10 + num % 10
            break
    x = str_num if x > 0 else -str_num
    if x < -2147483648 or x > 2147483647:
        return 0
    else:
        return x


def reverseInteger(x):
    num = abs(x)
    if num < 10:
        return x
    str_num = str(num)
    l, r = 0, len(str_num) - 1
    left = ''
    right = ''
    while l < r:
        left += str_num[r]
        right = str_num[l] + right
        l += 1
        r -= 1
    if l == r:
        str_num = int(left + str_num[l] + right)
    else:
        str_num = int(left + right)
    x = str_num if x > 0 else -str_num
    if x < -2147483648 or x > 2147483647:
        return 0
    else:
        return x

def reverse(x):
    num = abs(x)
    if num < 10:
        return x
    str_num = str(num)
    l = [0] * (len(str_num))
    i = 0
    while i <= (len(str_num)-1)//2:
        j = len(str_num) - 1 - i
        l[i] = str_num[j]
        l[j] = str_num[i]
        i += 1
    rev_num = int(''.join(l))
    x = rev_num if x > 0 else (-1)*rev_num
    if x < -2147483648 or x > 2147483647:
        return 0
    else:
        return x
import math

def reverseInteger(num):
    # num = abs(x)
    # if num < 10:
    #     return x
    # res_num = 0
    # while num // 10 != 0:
    #     rest = num % 10
    #     res_num = res_num * 10 + rest
    #     num = num // 10
    # # res_num = res_num*10 + num % 10
    # if res_num > 214748364:
    #     return 0
    # if res_num == 214748364 and num > 7:
    #     if x > 0 or num > 8 and x < 0:
    #         return 0
    # if res_num == 214748364 and num < 7:
    #     return res_num*10 + num if x > 0 else -(res_num*10 + num)
    # return res_num*10 + num if x > 0 else -(res_num*10 + num)
    res_num = 0
    while num != 0:
        rest = int(math.fmod(num, 10))
        num = int(num / 10)
        if res_num > 214748364 or (res_num == 214748364 and rest > 7):
            return 0
        if res_num < -214748364 or (res_num == -214748364 and rest < -8):
            return 0
        res_num = (res_num * 10) + rest
    return res_num


number = 8463847412
print(reverseInteger(number))

