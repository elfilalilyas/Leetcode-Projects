import time
# def fun(string):
#     k = len(string)
#     while k > 0:
#         L = 0
#         while True:
#             R = L + k
#             if R == len(string) + 1:
#                 break
#             s = string[L:R]
#             print(s)
#             rev_s = list(s)
#             rev_s.reverse()
#             if s == ''.join(rev_s):
#                 return s
#             L += 1
#         k -= 1
# def fun(s):
#     l = 0
#     r = len(s) - 1
#     st = ''
#     while l < len(s):
#         print('--', st)
#         print(l, r)
#         if s[l] == s[r]:
#             ss = s[l:r+1]
#             ss_list = list(ss)
#             if ss_list == ss_list[::-1]:
#                 print(ss)
#                 if len(ss) > len(st):
#                     st = ss
#                 l += 1
#                 r = len(s) - 1
#                 continue
#         if l == r:
#             l += 1
#             r = len(s) - 1
#             if l > r:
#                 break
#         r -= 1
#     return st
###-----
# else:
# st = s[c]
# while l >= 0 and r < len(s):
#     if s[l] != s[r]:
#         break
#     st = s[l] + st + s[r]
#     r += 1
#     l -= 1
# if len(st) > len(palindorm):
#     palindorm = st
# if s[c] == s[c + 1]:
#     st = s[c] + s[c + 1]
#     l = c - 1
#     r = c + 2
#     while l >= 0 and r < len(s):
#         if s[l] != s[r]:
#             break
#         st = s[l] + st + s[r]
#         r += 1
#         l -= 1
#     if len(st) > len(palindorm):
#         palindorm = st

## my method
def fun(s):
    palindorm = ''
    if len(s) == 1:
        return s
    for c in range(len(s) - 1):
        l, r = c - 1, c + 1
        st = s[c]
        # this for odd palindromic substring
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            st = s[l] + st + s[r]
            r += 1
            l -= 1
        if len(st) > len(palindorm):
            palindorm = st
        # this for even palindromic substring
        if s[c] == s[c+1]:
            st = s[c] + s[c + 1]
            l, r = c - 1, c + 2
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                st = s[l] + st + s[r]
                r += 1
                l -= 1
            if len(st) > len(palindorm):
                palindorm = st

    return palindorm

## the best method
def theLongestSubsS(s):
    palin = ''
    if len(s) <= 1:
        return s
    for c in range(len(s)):
        # for odd palindromic sub_S
        l, r = c, c
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # if the string is itself a palindrome, then it's the longest palindromic sub_s
            if r - l + 1 == len(s):
                return s
            if r - l + 1 > len(palin):
                palin = s[l:r+1]
            l -= 1
            r += 1
        # for even palindromic sub_s
        l, r = c, c + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # if the string is itself a palindrome, then it's the longest palindromic sub_s
            if r - l + 1 == len(s):
                return s
            if r - l + 1 > len(palin):
                palin = s[l:r + 1]
            l -= 1
            r += 1
    return palin

s = 'ttaat'
start = time.time()
print(theLongestSubsS(s))
print(time.time() - start)

