import sys

N = int(sys.stdin.readline().rstrip())
kids = list(map(int, sys.stdin.readline().split()))
dp = [0] * (N + 1)
for i in kids:
    dp[i] = dp[i - 1] + 1

print(N - max(dp))
