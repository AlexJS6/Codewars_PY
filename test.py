# -*- cofing:utf-8 -*

# https://www.w3schools.com/python/python_strings.asp check every data-strcture method (bottom of page here string)
# Continue at 'Operators'
#https://docs.python.org/3/tutorial/datastructures.html data structures python site
#https://thepythonguru.com/python-builtin-functions/reduce/ reduce
#at for loops


#import os

def activityNotifications(expenditure, d):
    freq = {}
    notify=0

    def find(idx):
        total_count = 0
        for i in range(201): 
            #print(freq)
            if i in freq:
                total_count = total_count + freq[i]
            if total_count >= idx:
                return i

    for i in range(len(expenditure)-1):
        #print(freq)
        if expenditure[i] in freq:
            freq[expenditure[i]]+=1
        else:
            freq[expenditure[i]]=1
        #print(f"i: {i},val: {expenditure[i]}, freq: {freq}")
        print('i:', i, 'd:', d)
        if i>=d-1:
            if d%2 ==0:
                median = (find(d//2)+find(d//2+1))/2
                print(median)
            else:
                median = find(d/2)
                print(median)
            #print("median: ",median)
            if expenditure[i+1]>= (median*2) :
                notify +=1
                print("notify: ",notify)
            #remove the previous element from dictionary
            freq[expenditure[i-d+1]]-=1

    return notify  


    




print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))#, 5






#os.system('pause')