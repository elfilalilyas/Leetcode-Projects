## wonderful solution
def strToInt(s):
    max_val = 2147483647
    min_val = -2147483648
    ret_num = 0
    signe = 1
    i = 0
    if s[0].isalpha():
        return ret_num
    else:
        while len(s) > 0 and s[0] == ' ':
            s = s[1:]
        if len(s) == 0:
            return ret_num
        if s[0] == '-':
            signe *= (-1)
            i += 1
        if s[0] == '+':
            i += 1
        while i < len(s) and s[i].isdigit():
            if (ret_num * signe > 214748364) or (ret_num * signe == 214748364 and int(s[i]) > 7):
                return max_val
            if (ret_num * signe < -214748364) or (ret_num * signe == -214748364 and int(s[i]) > 8):
                return min_val
            ret_num = ret_num * 10 + int(s[i])
            i += 1

    return ret_num * signe

def myAtoi(s):
    max_val = 2147483647
    min_val = -2147483648
    ret_num = 0
    signe = 1
    i = 0
    if len(s) == 0:
        return ret_num
    if s[0].isalpha():
        return ret_num
    else:
        while len(s) > 0 and s[0] == ' ':
            s = s[1:]
        if len(s) == 0:
            return ret_num
        if s[0] == '-':
            signe *= (-1)
            i += 1
        if s[0] == '+':
            i += 1
        while i < len(s) and s[i].isdigit():
            if (ret_num * signe > 214748364) or (ret_num * signe == 214748364 and int(s[i]) > 7):
                return max_val
            if (ret_num * signe < -214748364) or (ret_num * signe == -214748364 and int(s[i]) > 8):
                return min_val
            ret_num = ret_num * 10 + int(s[i])
            i += 1

    return ret_num * signe

st = "2147483646"
print(strToInt(st))