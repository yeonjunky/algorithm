import sys


INF = 10000000000

def dijkstra(start, direction):
    if direction == 1:
        d = to_n
    else:
        d = from_n

    dp = [INF] * N
    v = [0] * N
    v[start] = 1

    for i, t in enumerate(d[start]):
        dp[i] = t

    dp[start] = 0

    for i in range(N - 2):
        min = INF
        idx = 0

        for j, val in enumerate(dp):
            if min > val and not v[j]:
                idx = j
                min = val
        v[idx] = 1

        for j in range(N):
            if not v[j]:
                if 0 < dp[idx] + d[idx][j] < dp[j]:
                    dp[j] = dp[idx] + d[idx][j]

    return dp


N, M, X = map(int, sys.stdin.readline().split())
to_n = [[INF] * N for _ in range(N)]
from_n = [[INF] * N for _ in range(N)]

for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    to_n[end - 1][start - 1] = time
    from_n[start - 1][end - 1] = time

a = dijkstra(X - 1, 1)
b = dijkstra(X - 1, 0)
result = [0] * N

for i in range(N):
    result[i] = a[i] + b[i]
print(max(result))
