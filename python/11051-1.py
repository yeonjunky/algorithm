import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(min(k + 1, i + 1)):
        if j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10007

print(dp[n][k])