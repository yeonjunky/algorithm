import sys

input = sys.stdin.readline

n, k = map(int, input().split())
w = []
v = []
dp = [[0 for _ in range(k + 1)] for _ in range(n)]


for _ in range(n):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

for c in range(k + 1):
    if w[0] <= c:
        dp[0][c] = v[0]

for i in range(1, n):
    for c in range(1, k + 1):
        selected = 0
        not_selected = 0

        if w[i] <= c:
            selected = dp[i - 1][c - w[i]] + v[i]
        not_selected = dp[i - 1][c]

        dp[i][c] = max(selected, not_selected)

print(max(dp[n - 1]))