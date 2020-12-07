# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce
#at for loops


#import os

#https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
def minimumAbsoluteDifference(arr):
    pos = abs(arr[0] - arr[1])
    for i, x in enumerate(arr): 
        while i < len(arr)-1:
            if pos > abs(x - arr[i +1]):
                pos = abs(x - arr[i +1])
            print('x:', x, 'other', arr[i+1], abs(x - arr[i+1]))
            i += 1
    return pos









print(minimumAbsoluteDifference([1, -3, 71, 68, 17]))











#os.system('pause')