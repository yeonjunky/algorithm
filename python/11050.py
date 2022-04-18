import sys

def factorial(n):
    dp = [0] * (n + 1)

    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]

    return dp[n]

input = sys.stdin.readline

n, k = map(int, input().split())

print(factorial(n) // (factorial(n - k) * factorial(k)))