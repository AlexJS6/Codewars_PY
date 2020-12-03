# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce
#at for loops


#import os

#https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def sherlockAndAnagrams(s):
    my_dict = {}
    for first in range(len(s)):
        for second in range(first +1, len(s)+1):
            result = ''.join(sorted(s[first:second]))
            if result in my_dict:
                my_dict[result] += 1
            else:
                my_dict[result] = 1
    
    count = 0
    for m, n in my_dict.items():
        count += n*(n-1)/2
        print(n*(n-1)/2)

    return int(count)

    




print(sherlockAndAnagrams('ifailuhkqq')) #3
#print(sherlockAndAnagrams('kkkk')) #10















#os.system('pause')