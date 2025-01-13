import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = {
    i: [] for i in range(n)
}
distance = [-1] * n

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)

distance[x - 1] = 0
dq = deque([x - 1])

while dq:
    v = dq.popleft()
    for i in graph[v]:
        if distance[i] == -1:
            dq.append(i)
            distance[i] = distance[v] + 1

for i in range(n):
    if distance[i] == k:
        print(i + 1)
        x = 0

if x:
    print(-1)