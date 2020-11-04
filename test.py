# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce



#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
'''def snail(snail_map):
    result = []
    length = len(snail_map)
    i = j = k = l = 0
    ii = jj = kk = ll = length
    while len(result) != (length * length):
        #horizontal_right
        for i in range(length -i):
            result.append(snail_map[j][i])
        i += i
        for (j + 1) in range(length - j):
            result.append(snail_map[j+1][length - j])
        j += 1
        for (length - i) in range (i -1):
            result.append(snail_map[length -i +1][])'''





array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array))#, expected) expected = [1,2,3,6,9,8,7,4,5]


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(array))#, expected) expected = [1,2,3,4,5,6,7,8,9]
