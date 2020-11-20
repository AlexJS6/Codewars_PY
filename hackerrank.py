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