# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce
#at for loops


#import os





#https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen
def alternatingCharacters(s):
    count = 0
    for x in range(len(s)-1):
        if s[x] == s[x+1]:
            count += 1
    return count





print(alternatingCharacters('BBBBB')) #4
print(alternatingCharacters('ABABABAB')) #0
print(alternatingCharacters('BABABA')) #0
print(alternatingCharacters('AAABBB')) #4









#os.system('pause')