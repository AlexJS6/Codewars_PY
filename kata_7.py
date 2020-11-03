#https://www.codewars.com/kata/54ff3102c1bad923760001f3
def get_count(input_str):
    num_vowels = 0
    for letter in input_str:
        if (letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'u' or letter.lower() == 'i' or letter.lower() == 'o'):
            num_vowels += 1
    
    return num_vowels

def getCount(inputStr):
   return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])