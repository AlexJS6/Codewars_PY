# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site


#https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
def reverse_words(text):
    my_list, result = text.split(' '), []
    for word in my_list:
        result.append(''.join(reversed(word)))
    return ' '.join(result)



print(reverse_words('The quick brown fox jumps over the lazy dog.'))#, 'ehT kciuq nworb xof spmuj revo eht yzal .god')
print(reverse_words('apple'))#, 'elppa')
print(reverse_words('a b c d'))#, 'a b c d')
print(reverse_words('double  spaced  words'))#, 'elbuod  decaps  sdrow')
