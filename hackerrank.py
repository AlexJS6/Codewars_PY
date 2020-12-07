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
def activityNotifications(expenditure, d):
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

#First optimization with slicing
def activityNotifications(expenditure, d):
    result = i = 0
    days = d
    def median(arr): #function that I call to calculate the median (parameter is already a sorted list)
        if len(arr) % 2 != 0:
            return arr[len(arr)//2]
        else:
            return arr[len(arr)//2 -1] + ((arr[len(arr)//2] - arr[len(arr)//2 -1]) / 2)

    while days <= len(expenditure) -1: #loops until reaches a list that let's 1 value to check
        a = median(sorted(expenditure[i:days])) #slices the d needed days
        if a * 2 <= expenditure[days]:
            result += 1
        days += 1
        i += 1
    return result
    
#Second optimization but still timing out
from statistics import median
def activityNotifications(expenditure, d):
    result = i = 0
    while i + d <= len(expenditure) -1: #loops until reaches a list that let's 1 value to check
        a = median(sorted(expenditure[i:i+d])) #slices the d needed days
        if a * 2 <= expenditure[i+d]:
            result += 1
        i += 1
    return result

# This one is working using frequency tables:
def activityNotifications(expenditure, d):
    freq = {}
    notify=0
    def find(idx):
        total_count = 0
        for i in range(201): 
            if i in freq:
                total_count = total_count + freq[i]
            if total_count >= idx:
                return i
    for i in range(len(expenditure)-1):
        if expenditure[i] in freq:
            freq[expenditure[i]]+=1
        else:
            freq[expenditure[i]]=1
        #print(f"i: {i},val: {expenditure[i]}, freq: {freq}")
        if i>=d-1:
            if d%2 ==0:
                median = (find(d//2)+find(d//2+1))/2
            else:
                median = find(d/2)
            #print("median: ",median)
            if expenditure[i+1]>= (median*2) :
                notify +=1
                print("notify: ",notify)
            #remove the previous element from dictionary
            freq[expenditure[i-d+1]]-=1
    return notify  




#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
from collections import Counter

def makeAnagram(a, b):
    counterA = Counter(a)
    counterB = Counter(b)
    result = 0
    for x in counterA & counterB:
        result += (counterA & counterB)[x]

    return (len(a) + len(b)) - result * 2




#https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen
def alternatingCharacters(s):
    count = 0
    for x in range(len(s)-1):
        if s[x] == s[x+1]:
            count += 1
    return count



#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def isValid(s):
    #return Counter(s).most_common()
    counts = Counter(map(lambda x:x[1], Counter(s).most_common()))
    return counts
    lcounts = sorted(counts.most_common())
    #return lcounts
    l = len(lcounts)
    #return lcounts[0][0]+1, 1
    if l == 2 and ((lcounts[0] == (1,1) or lcounts[1] == (lcounts[0][0]+1,1))):
        return "YES"
    return "YES" if l == 1 else "NO"




#https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
# Too slow but working
from collections import Counter
def substrCount(n, s):
    #return s[0:3][::-1]
    count = i = 0
    letter = ''
    while i < n+1:
        for x in range(i+1, n+1):
            if len(tuple(Counter(s[i:x]))) > 1:
                letter = tuple(Counter(s[i:x]))[1]
            #return Counter(s[i:x])[letter]
            if s[i:x] == s[i:x][::-1] and len(Counter(s[i:x])) < 3 and Counter(s[i:x])[letter] < 2:
                count += 1
                #print(s[i:x])
        i += 1
    return count

#optimized and working
def substrCount(n, s):
    l = []
    count = 0
    cur = None

# 1st pass
    for i in range(n):
        if s[i] == cur:
            #return s[i]
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
            #print(l)
    l.append((cur, count))
    #print(l)

    ans = 0
		
# 2nd pass
    for i in l:
        #return i[1]
        #return (i[1] * (i[1] +1)) // 2
        ans += (i[1] * (i[1] + 1)) // 2
        #print(ans)
    #return ans

# 3rd pass
    for i in range(1, len(l) - 1):
        #return l[i -1]
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            #return 'YE'
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans




#https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def sherlockAndAnagrams(s):
    my_dict = {}
    for first in range(len(s)):
        for second in range(first +1, len(s)+1):
            result = ''.join(sorted(s[first:second]))
            if result in my_dict:
                my_dict[result] += 1
            else:
                my_dict[result] = 1
    
    count = 0
    for m, n in my_dict.items():
        count += n*(n-1)/2
        print(n*(n-1)/2)

    return int(count)




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

# Shorter
def luckBalance(k, contests):
    important = sorted([s[0] for s in contests if s[1] == 1], reverse = True)
    unimportant = [s[0] for s in contests if s[1] == 0]
    return sum(important[:k])-sum(important[k:])+sum(unimportant)




#https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
def minimumAbsoluteDifference(arr):
    pos = abs(arr[0] - arr[1])
    for i, x in enumerate(arr): 
        while i < len(arr)-1:
            if pos > abs(x - arr[i +1]):
                pos = abs(x - arr[i +1])
            print('x:', x, 'other', arr[i+1], abs(x - arr[i+1]))
            i += 1
    return pos