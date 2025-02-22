# method 1
def fun(s):
    palindorm = ''
    if len(s) == 1:
        return s
    for c in range(len(s) - 1):
        l, r = c - 1, c + 1
        st = s[c]
        # for odd palindromic substring
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            st = s[l] + st + s[r]
            r += 1
            l -= 1
        if len(st) > len(palindorm):
            palindorm = st
        # for even palindromic substring
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

# method 2
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

