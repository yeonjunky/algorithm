import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
num_edge = [0] * N
edge = {i: [] for i in range(1, N + 1)}
queue = deque()
result = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    num_edge[b - 1] += 1

for i in range(N):
    if num_edge[i] == 0:
        queue.append(i + 1)
        num_edge[i] = -1

for _ in range(N):
    node = queue.popleft()
    result.append(node)

    for n in edge[node]:
        num_edge[n - 1] -= 1

        if num_edge[n - 1] == 0:
            queue.append(n)
            num_edge[n - 1] = -1

print(*result)
