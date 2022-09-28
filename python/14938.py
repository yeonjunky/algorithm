import sys

INF = 300000
N, M, R = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))
adj = [[INF] * N for _ in range(N)]
num_item = [0] * N

for i in range(N):
    for j in range(N):
        if i == j:
            adj[i][j] = 0

for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().split())
    adj[b - 1][a - 1] = l
    adj[a - 1][b - 1] = l

for k in range(N):
    for i in range(N):
        for j in range(N):
            m = min(adj[i][j], adj[i][k] + adj[k][j])
            adj[i][j] = m

for i in range(N):
    for j in range(N):
        if adj[i][j] <= M:
            num_item[i] += T[j]

print(max(num_item))
