import sys

N = int(sys.stdin.readline().rstrip())
turn_cnt = 0
dp = [-1] * (N + 1)
result = ''

for i in range(1, 4):
    if N >= i:
        dp[i] = i % 2

for i in range(4, N + 1):
    if dp[i - 3] == 1:
        dp[i] = 2
    else:
        dp[i] = 1

if dp[N] == 1:
    result = 'SK'
else:
    result = 'CY'

print(result)
