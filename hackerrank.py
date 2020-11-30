#Easy
#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def sockMerchant(n, ar):
    result,done = 0, []
    for i in range(n):
        test_arr = []
        for j in range(n):
            if (ar[i] == ar[j]) and (ar[j] not in done):
                test_arr.append(ar[j])
        print(done)
        if len(test_arr) > 0:   
            done.append(test_arr[0])
        result += len(test_arr) // 2
    return result



#Easy
# #https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
def countingValleys(steps, path):
    level, num, result = 'above', 0, 0
    for step in path:
        if step == 'U':
            num += 1
            if num == 0 and level == 'under':
                level = 'above'
        if step == 'D':
            num -= 1
            if num < 0 and level == 'above':
                result += 1
                level ='under'
    return result



#Easy
#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def jumpingOnClouds(c):
    i = result = 0
    while i < len(c):
        if i < len(c) -2:
            if c[i] == 0 and c[i+1] == 0 and c[i+2] == 0:
                result += 1
                i += 2 
                continue
        if c[i] == 0:
            result += 1
            i += 1
        else:
            i += 1
    return result -1



#Easy but pretty proud of my formula
#https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def repeatedString(s, n):
    rest = n % len(s)
    new_num = n - rest
    x = s.count('a')
    y = len(s)
    return math.ceil((new_num/y) * x) + s[:rest].count('a')



#https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def hourglassSum(arr):
    i, result = 0, []
    while i < len(arr) -2:
        for x in range(len(arr)-2): #i = cols, x = rows
            my_int = arr[i][x] + arr[i][x+1] + arr[i][x+2] + arr[i+1][x+1] + arr[i+2][x] + arr[i+2][x+1] + arr[i+2][x+2]
            result.append(my_int)
        i += 1
    return max(result)



#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen
def rotLeft(d, a):
    i = 0
    while i < a:
        num = d[0]
        d.pop(0)
        d.append(num)
        i += 1
    return d



#https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def minimumBribes(q):
    moves = 0 
    q = [p-1 for p in q]
    for i,p in enumerate(q):  
        if p - i > 2:
            print('Too chaotic')
            return
        for j in range(max(p-1,0),i):
            if q[j] > p:
                moves += 1
    print(moves)



#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minimumSwaps(arr):
    x = result = 0
    while x < len(arr):
        if arr[x] != x +1:
            swapper = arr[x] #3
            index = arr.index(x+1)
            arr[x] = arr[index]
            arr[index] = swapper
            result += 1
        x += 1
    
    return (arr, result)
#Optimized with hashtables:
def minimumSwaps(arr):
    sorted_list = sorted(arr)
    index_dict = {i: x for x, i in enumerate(arr)}
    result = 0

    for x, i in enumerate(arr):
        correct = sorted_list[x]
        if i != correct:
            swapper = index_dict[correct]
            arr[swapper], arr[x] = arr[x], arr[swapper]
            index_dict[i] = swapper
            index_dict[correct] = x
            result += 1
    return result



#https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
def countSwaps(a):
    correct = sorted(a)
    result = 0
    while True:
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                result += 1
        if correct == a:
            break
    print(f'Array is sorted in {result} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')



#https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
def maximumToys(prices, k):
    result, sorted_prices = 0, sorted(prices)
    for x in sorted_prices:
        if x <= k:
            result += 1
            k -= x
    return result



#https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
from collections import Counter
def checkMagazine(magazine, note):
    a = Counter(magazine)
    b = Counter(note)
    print("Yes" if a & b == b else "No")



#https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen
def twoStrings(s1, s2):
    for x in s1:
        if x in s2:
            return 'YES'
    return 'NO'



#https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return self.name
        
    def comparator(a, b):
        if a.score > b.score: return -1 
        if a.score < b.score: return 1 # Does the scores first
        if a.name > b.name: return 1    # if not greater or smaller check names
        if a.name < b.name: return -1   #if names not greater or less return 0
        return 0





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