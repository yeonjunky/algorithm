import sys

t = int(sys.stdin.readline().replace('\n', ''))

for i in range(t):
    n = int(sys.stdin.readline().replace('\n', ''))
    dp = [0] * n

    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for j in range(3, n):
        dp[j] = dp[j - 2] + dp[j - 3]

    print(dp[n - 1])