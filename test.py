# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
from math import *
def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        return s[int(length/2-1)] + s[int(length/2)]
    else:
        return s[floor(length/2)]


print(get_middle("test"))#,"es")
print(get_middle("testing"))#,"t")
print(get_middle("middle"))#,"dd")
print(get_middle("A"))#,"A")
print(get_middle("of"))#,"of")