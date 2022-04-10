import sys

k = int(sys.stdin.readline().rstrip())
dp = [[0, 0] for _ in range(k + 1)]

dp[0] = [1, 0]

for i in range(1, k + 1):

    dp[i][0] +=  dp[i - 1][1]
    dp[i][1] += (dp[i - 1][0] + dp[i - 1][1])

print(dp[k][0], dp[k][1])
