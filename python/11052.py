import sys

n = int(sys.stdin.readline().rstrip())
p = [0]
p.extend(list(map(int, sys.stdin.readline().split())))
dp = [i for i in p]

for i in range(1, n + 1):
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i - j] + p[j], dp[i])

print(dp[n])
