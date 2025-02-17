import sys

def factorial(dp, n):
    dp[0] = 1

    if dp[n]:
        return dp[n]

    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]
    return dp[n]

t = int(sys.stdin.readline())
dp = [0] * 31

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(factorial(dp, m) // (factorial(dp, n) * factorial(dp, m - n)))