import sys

def factorial(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]

    return dp[n]


t = int(sys.stdin.readline().replace('\n', ''))

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split(' '))

    print(int(factorial(m) / (factorial(n) * factorial(m - n))))
