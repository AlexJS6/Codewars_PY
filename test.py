# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce
#at for loops


#import os

#Use slice!!
#https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zentivityNotifications(expenditure, d):
from statistics import median
def activityNotifications(expenditure, d):
    result = i = 0
    while i + d <= len(expenditure) -1: #loops until reaches a list that let's 1 value to check
        a = median(sorted(expenditure[i:i+d])) #slices the d needed days
        if a * 2 <= expenditure[i+d]:
            result += 1
        i += 1
    return result




'''def activityNotifications(expenditure, d):
count = 0
for i in range(0, len(expenditure)-d):
    med = statistics.median(expenditure[i:i+d])
    if expenditure[i+d] >= med*2:
        count +=1
return count'''

    




print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))#, 5






#os.system('pause')