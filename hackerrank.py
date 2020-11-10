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

#Easy#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
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
