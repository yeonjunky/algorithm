import sys

n, m = map(int, sys.stdin.readline().split(' '))
area = [[0] for j in range(n + 1)]

for i in range(1, n+1):
    area[i].extend(list(map(int, sys.stdin.readline().split(' '))))

k = int(sys.stdin.readline().replace('\n', ''))


dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
dp[1][1] = area[1][1]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + area[i][j]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)
