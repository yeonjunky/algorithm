import sys


n = int(sys.stdin.readline().rstrip())
dp = [-1] * (n + 1)

dp[0] = 1

if n > 0:
    dp[1] = 1

for i in range(2, n + 1):
    sum = 0

    for j in range(i):
        sum += dp[j] * dp[(i - 1) - j]

    dp[i] = sum

print(dp[n])
