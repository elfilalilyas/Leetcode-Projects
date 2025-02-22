# def zigzag_conversion(string, row):
#     k = (row-1) * 2 if row > 1 else 1
#     zigzag_str = ''
#     l = [*range(0, len(string) + 1, k)]
#     indexes = l
#     print(indexes)
#     for i in range(1, row):
#         if i == row - 1:
#             for m in range(i, len(string), k):
#                 if m not in indexes:
#                     indexes.append(m)
#             print(i, indexes)
#         else:
#             j = 0
#             while j < len(l):
#                 n = l[j]
#                 print('------------------', abs(n-i), n, n + 1)
#                 if abs(n-i) not in l:
#                     if abs(n-i) >= len(string):
#                         break
#                     indexes.append(abs(n-i))
#                 if n+i not in l:
#                     if n + i >= len(string):
#                         break
#                     indexes.append(n + i)
#                 j += 1
#             # # l = set([abs(n-1) for n in l if abs(n-1) > 0] + [n+1 for n in l if n + 1 < len(string)])
#             # l += sorted([abs(n - 1) for n in l if abs(n - 1) > 0 and abs(n-1) not in l] + [n + 1 for n in l if n + 1 < len(string) and n + 1 not in l])
#             # indexes += [abs(n-i) for n in l if abs(n-i) not in indexes]
#             # indexes += [n+i for n in l if n+i not in indexes]
#             print(i, indexes)
#     for j in indexes:
#         if j < len(string):
#             zigzag_str += string[j]
#     return zigzag_str


#### using matrix
# def zigzag_conversion(string, row):
#     if row == 1:
#         return string
#     matrix = [[] for _ in range(row)]
#     i = 0
#     l = 0
#     d = +1
#     while i < len(string):
#         n = string[i]
#         matrix[l].append(n)
#         if l == row - 1:
#             d = -1
#         if l == 0:
#             d = +1
#         l += d
#         i += 1
#     return ''.join([''.join(line) for line in matrix])

### using hashmap
# def zigzag_conversion(string, row):
#     if row == 1:
#         return string
#     dic = {}
#     for _ in range(row):
#         dic[_] = []
#     i = 0
#     l = 0
#     d = +1
#     while i < len(string):
#         n = string[i]
#         # matrix[l].append(n)
#         dic[l].append(n)
#         if l == row - 1:
#             d = -1
#         if l == 0:
#             d = +1
#         l += d
#         i += 1
#     return ''.join([''.join(dic[line]) for line in dic])
#
# ### using simple list
# def zigzag_conversion(string, row):
#     if row == 1:
#         return string
#     matrix = ['' for _ in range(row)]
#     i = 0
#     l = 0
#     d = +1
#     while i < len(string):
#         n = string[i]
#         matrix[l] += n
#         if l == row - 1:
#             d = -1
#         if l == 0:
#             d = +1
#         l += d
#         i += 1
#     return ''.join(matrix)


#### this is my best
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


### the Solution of neetcode
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

s = "PAYPALISHIRING"
numRows = 3
print(zigzag_conversion(s, numRows))
#      PINALSIG YAHRPI
#      PINALSIG YAHRPI
# 4    PINALSIG YAHRPI
#      PAHNAPLSIIGYIR
#      PAHNAPLSIIGYIR
# 3    PAHNAPLSIIGYIR



