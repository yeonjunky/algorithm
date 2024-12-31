import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
cnt = 0

for i in range(n):
    coins.append(int(sys.stdin.readline()))

for i in range(n - 1, -1, -1):
    c = k // coins[i]
    if c:
        cnt += c
        k -= coins[i] * c

print(cnt)