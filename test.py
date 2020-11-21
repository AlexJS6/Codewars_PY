# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce
#at for loops


import os


#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minimumSwaps(arr):
    x = result = 0
    while x < len(arr):
        if arr[x] != x +1:
            arr[x], arr[arr.index(x+1)] = arr[arr.index(x+1)], arr[x]
            '''swapper = arr[x] #3
            index = arr.index(x+1)
            arr[x] = arr[index]
            arr[index] = swapper
            result += 1'''
        x += 1
    
    return (arr, result)





print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))







os.system('pause')