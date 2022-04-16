import sys

input = sys.stdin.readline

c, n = map(int, input().split())
dp = [1000000] * (c + 100)
dp[0] = 0
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x : x[0])

for cost, client in data:
    for i in range(client, c + 100):
        dp[i] = min(dp[i - client] + cost, dp[i])

print(min(dp[c:]))
