## There are a lot of ways to solve this problem. the difference between them relies on time and space complexity
## the two last ways are the best.

# 1/-----------------------------------------------------------
# def longest_subs(s):
#     m = 1
#     if len(s) <= 1:
#         return m * len(s)
#     else:
#         i = 0
#         j = i
#         c = 1
#         while True:
#             chars = s[i:j+2]
#             if chars[-1] not in chars[:-1]:
#                 c += 1
#                 j += 1
#                 if c > m:
#                     m = c
#             else:
#                 i += 1
#                 j = i
#                 c = 1
#             if j == len(s) - 1:
#                 break
#     return m
#--------------------------------------------------------------


# 2/-----------------------------------------------------------
# def longest_subs(s):
#     l = len(s)
#     for i in range(l, -1, -1):
#         j = 0
#         while j + i <= l:
#             bol = True
#             chars = s[j:j+i]
#             for char in chars:
#                 if chars.count(char) > 1:
#                     bol = False
#                     break
#             if bol:
#                 return i, chars
#             j += 1
#--------------------------------------------------------------


# 3/-----------------------------------------------------------
# def longest_subs(s):
#     subs_long = ('', 0)
#     for i, char in enumerate(s):
#         chars = ''
#         c = 0
#         while i <= len(s) - 1:
#             char = s[i]
#             if char not in chars:
#                 chars += char
#                 c += 1
#                 i += 1
#                 if c > subs_long[-1]:
#                     subs_long = (chars, c)
#             else:
#                 break
#
#
#     return subs_long
#-------------------------------------------------------------

# 4/-----------------------------------------------------------
## the difference here is that used list() instead set()
# def longest_subs(s):
#     long_sub = []
#     m = 0
#     for i in s:
#         if i not in long_sub:
#             long_sub.append(i)
#             m = len(long_sub) if len(long_sub) > m else m
#         else:
#             while True:
#                 if i in long_sub:
#                     long_sub.pop(0)
#                 else:
#                     long_sub.append(i)
#                     break
#     return m
#
# l_subs = longest_subs("abcabcbb")
# print(l_subs)
#-----------------------------------------------------------

# 5/-----------------------------------------------------------
# def longest_subs(s):
#     long_sub = set()
#     m = 0
#     i = 0
#     for ind, char in enumerate(s):
#         if char not in long_sub:
#             long_sub.add(char)
#             m = len(long_sub) if len(long_sub) > m else m
#         else:
#             for j in range(i, ind):
#                 print(j, ind)
#                 print(long_sub, char)
#                 long_sub.remove(s[j])
#                 i = j + 1
#                 if char not in long_sub:
#                     long_sub.add(char)
#                     print(long_sub)
#                     break
#
#     return m
#
# l_subs = longest_subs("abcdbfal")
# print(l_subs)
#-----------------------------------------------------------

# 6/-----------------------------------------------------------
## The solution of the youtuber
# def longest_subs(s):
#     long_sub = set()
#     m = 0
#     j = 0
#     for i in range(len(s)):
#         '''if s[r] is in sub_long then we keep deleting items from the start of string s
#         until the s[r] is no longer in long_sub'''
#         while s[i] in long_sub:
#             long_sub.remove(s[j])
#             j += 1
#         '''if s[r] not in long_sub'''
#         long_sub.add(s[i])
#         if i-j+1 > m:
#             m = i-j+1
#         # m = max(m, i-j+1)
#     return m
#
# l_subs = longest_subs("abcdbfal")
# print(l_subs)
#-----------------------------------------------------------

# 7/-----------------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_sub = set()
        m = 0
        j = 0
        for i in range(len(s)):
            while s[i] in long_sub:
                long_sub.remove(s[j])
                j += 1
            long_sub.add(s[i])
            m = max(m, i-j+1)
        return m
