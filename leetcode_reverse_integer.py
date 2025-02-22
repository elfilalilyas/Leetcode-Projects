# Method 1
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

# Method 2
def reverseInteger(num):
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



