# Method 1
def zigzag_conversion(s, row):
    if row == 1:
        return s
    k = 2 * (row - 1)
    st = ''
    for i in range(row):
        if i == 0 or i == row - 1:
            for _ in range(i, len(s), k):
                st += s[_]
        else:
            j = i
            while True:
                if j == i:
                    if j >= len(s):
                        break
                    st += s[j]
                else:
                    if j - (i * 2) >= len(s):
                        break
                    st += s[j - (i * 2)]
                    if j >= len(s):
                        break
                    st += s[j]
                j += k
    return st


# Method 2
def zigzag_conversion(s, row):
    if row == 1:
        return s
    k = 2 * (row - 1)
    st = ''
    for i in range(row):
        for j in range(i, len(s), k):
            letter = s[j]
            st += letter
            missed = (j + k) - (2 * i)
            if i != 0 and i != row - 1 and missed < len(s):
                st += s[missed]
    return st



