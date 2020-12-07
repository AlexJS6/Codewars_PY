# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce
#at for loops


#import os

#https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
def luckBalance(k, contests):
    result = 0
    important = []
    for contest in contests:
        if contest[1] == 1:
            important.append(contest)
        else:
            result += contest[0]
            print(contest[0])
    sorted_important = sorted(important, reverse=True)
    for x in range(len(sorted_important)):
        if x >= k :
            result -= sorted_important[x][0]
            print('substraction:', sorted_important[x][0], 'x:', x)
        else:
            result += sorted_important[x][0]
            print('addition:', sorted_important[x][0], 'x:', x)
    return result
    # to return sorted on [1] -> return sorted(important, key = lambda x: x[1], reverse = True)





print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))












#os.system('pause')