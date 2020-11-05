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
    return number'''