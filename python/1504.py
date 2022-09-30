import sys


def dijkstra(start):
    dp = [INF] * N
    v = [0] * N

    for i, c in enumerate(adj[start]):
        dp[i] = c

    dp[start] = 0
    v[start] = 1

    for i in range(N - 2):
        idx = 0
        min = INF

        for j, c in enumerate(dp):
            if c < min and not v[j]:
                idx = j
                min = c
        v[idx] = 1

        for j in range(N):
            if not v[j]:
                if dp[idx] + adj[idx][j] < dp[j]:
                    dp[j] = adj[idx][j] + dp[idx]
    return dp


INF = 9990000000
N, E = map(int, sys.stdin.readline().split())
adj = [[INF] * N for _ in range(N)]

for _ in range(E):
    s, e, c = map(int, sys.stdin.readline().split())
    adj[s - 1][e - 1] = c
    adj[e - 1][s - 1] = c

v1, v2 = map(int, sys.stdin.readline().split())

d1 = dijkstra(v1 - 1)
d2 = dijkstra(v2 - 1)
min_cost = min(d1[0] + d1[v2 - 1] + d2[N - 1], d2[0] + d2[v1 - 1] + d1[N - 1])
print(min_cost if min_cost < INF else -1)
