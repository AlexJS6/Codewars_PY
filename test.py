# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce
#at for loops


#import os

#Use slice!!
#https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zentivityNotifications(expenditure, d):
    result = i = 0
    days = d
    sorted_list = sorted(expenditure)
    def median(arr): #function that I call to calculate the median (parameter is already a sorted list)
        if len(arr) % 2 != 0:
            return arr[len(arr)//2]
        else:
            return arr[len(arr)//2 -1] + ((arr[len(arr)//2] - arr[len(arr)//2 -1]) / 2)

    while days <= len(expenditure) -1: #loops until reaches a list that let's 1 value to check
        temporary_list = []
        for x in range(i, days):
            temporary_list.append(expenditure[x]) #new list that always gets checked
        a = median(sorted(temporary_list))
        if a * 2 <= expenditure[days]:
            result += 1
        days += 1
        i += 1
    return result

    




print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))#, 5






#os.system('pause')