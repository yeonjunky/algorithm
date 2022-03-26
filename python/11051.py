import sys

def factorial(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]

    return dp[n]

n, k = map(int, sys.stdin.readline().split(' '))

result = factorial(n) // (factorial(k) * factorial(n - k))

print(result % 10007)
