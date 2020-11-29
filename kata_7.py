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

#optimized
def find_short(s):
    return min(len(x) for x in s.split())




#https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
def reverse_words(text):
    my_list, result = text.split(' '), []
    for word in my_list:
        result.append(''.join(reversed(word)))
    return ' '.join(result)

#optimized
def reverse_words(str):
  return ' '.join(w[::-1] for w in str.split(' '))



#https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return sum(numbers[:2])



#https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(string):
    for x in string:
        if x.lower() in 'aeoiu':
            string = string.replace(x, '')
    return string

#optimized:
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s



#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
def accum(s):
    x, result = 1, ''
    for i in s:
        for j in range(0 ,x):
            result += i.lower()
        result += '-'
        x += 1
    return result.title()[:len(result)-1]

#optimized:
def accum(s):
    return '-'.join([c.upper() + c.lower() * i for i, c in enumerate(s)])




#https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
def xo(s):
    print(s)
    exes = ohs = 0
    for letter in s:
        if letter.lower() == 'x':
            exes += 1
        if letter.lower() == 'o':
            ohs += 1
    return True if exes == ohs else False