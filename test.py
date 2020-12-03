# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce
#at for loops


#import os


#find max valu
#max vs sum

from collections import Counter


#https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def substrCount(n, s):
    #return s[0:3][::-1]
    count = i = 0
    letter = ''
    while i < n+1:
        for x in range(i+1, n+1):
            if len(tuple(Counter(s[i:x]))) > 1:
                letter = tuple(Counter(s[i:x]))[1]
            #return Counter(s[i:x])[letter]
            if s[i:x] == s[i:x][::-1] and len(Counter(s[i:x])) < 3 and Counter(s[i:x])[letter] < 2:
                count += 1
                print(s[i:x])
        i += 1
    return count

#working
def substrCount(n, s):
    l = []
    count = 0
    cur = None

# 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0
		
# 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

# 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans








print(substrCount(7, 'abcbaba'))
#abcbaba


















#os.system('pause')