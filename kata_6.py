#https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
def find_it(seq):
        if seq.count(num) % 2 != 0 for num in seq:
            return num



#https://www.codewars.com/kata/54e6533c92449cc251001667/solutions/python 
def unique_in_order(iterable):
    result = ['ö']
    for c in iterable:
        if result[len(result)-1] != c:
            result.append(c)
    result.remove('ö')
    return result




#https://www.codewars.com/kata/541c8630095125aba6000c00/solutions/python
def digital_root(number):
    while len(str(number)) > 1:
        new_arr = []
        for c in str(number):
            new_arr.append(int(c))
        number = sum(new_arr)
    return number



#https://www.codewars.com/kata/5266876b8f4bf2da9b000362
def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return '{} likes this'.format(names[0])
    if len(names) == 2:
        return '{} and {} like this'.format(names[0], names[1])
    if len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    if len(names) > 3:
        return '{}, {} and {} others like this'.format(names[0], names[1], (len(names)-2)) 

#optimized
def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.
    
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others = length - 2)




#https://www.codewars.com/kata/526571aae218b8ee490006f4
def count_bits(n):
    bine, add = bin(n).replace('0b', ''), 0
    for c in bine: 
        if c == '1': add += 1
    return add

#optimized
countBits = lambda n: bin(n).count('1')



#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
def array_diff(a, b):
    for bchar in b:
        for achar in a:
            if bchar == achar:
                a.remove(bchar)
                array_diff(a, b)
    return a