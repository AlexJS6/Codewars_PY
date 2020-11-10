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

    