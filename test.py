# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce
#at for loops


import os



from collections import Counter


string = ['hi', 'heya', 'hi']

x = Counter(string)
print(x)


'''def checkMagazine(magazine, note):
    #Count all words in magazine
    #Counter({'two': 1, 'times': 1, 'three': 1, 'is': 1, 'not': 1, 'four': 1})
    a = Counter(magazine)
    
    #Count all words in note
    #Counter({'two': 2, 'times': 1, 'is': 1, 'four': 1})
    b = Counter(note)
    
    # a & b - a intersection b
    # Counter({'two': 1, 'times': 1, 'is': 1, 'four': 1})
    return "Yes" if ( a & b ) == b else "No"

m,n = map(int,input().split())
magazine = input().split()
note = input().split()
print(checkMagazine(magazine, note))'''






os.system('pause')