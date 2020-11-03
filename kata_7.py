#https://www.codewars.com/kata/54ff3102c1bad923760001f3
def get_count(input_str):
    num_vowels = 0
    for letter in input_str:
        if (letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'u' or letter.lower() == 'i' or letter.lower() == 'o'):
            num_vowels += 1
    
    return num_vowels
#optimized
def getCount(inputStr):
   return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])



#https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
from math import *
def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        return s[int(length/2-1)] + s[int(length/2)]
    else:
        return s[floor(length/2)]



#https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
def square_digits(num):
    string, result = str(num), ''
    for num in string:
        mysqr = str(int(num) * int(num))
        result += mysqr
    return int(result)



#https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
def find_short(s):
    new_list, num = s.split(' '), 100
    for word in new_list:
        if len(word) < num: num = len(word)
    return num