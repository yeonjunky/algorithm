import sys

def fibo(n):
    memo = [0, 1]

    for i in range(2, n + 1):
        memo.append(memo[i-1] + memo[i-2])

    return memo[n]

n = int(sys.stdin.readline().replace('\n', ''))


print(fibo(n))

