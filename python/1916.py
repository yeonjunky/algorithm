import sys


INF = 1000000000

def dijkstra(start):
    dp = [INF] * N
    visited = [0] * N
    visited[start] = 1

    for i, c in enumerate(adj[start]):
        dp[i] = c
    dp[start] = 0

    for i in range(N - 2):
        idx = 0
        min = INF
        for j, c in enumerate(dp):
            if c < min and not visited[j]:
                idx = j
                min = c
        visited[idx] = 1

        for j in range(N):
            if not visited[j]:
                if dp[idx] + adj[idx][j] < dp[j]:
                    dp[j] = adj[idx][j] + dp[idx]
    return dp

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
adj = [[INF] * N for _ in range(N)]

for _ in range(M):
    city1, city2, cost = map(int, sys.stdin.readline().split())
    adj[city1 - 1][city2 - 1] = min(adj[city1 - 1][city2 - 1], cost)

for i in range(N):
    for j in range(N):
        if i == j:
            adj[i][j] = 0

start, end = map(int, sys.stdin.readline().split())
print(dijkstra(start - 1)[end - 1])
