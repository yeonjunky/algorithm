import sys
from collections import deque


def bfs(n, distance):
    queue = deque([n])
    visited[n] = True

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i[0]]:
                queue.append(i[0])
                distance[i[0]] = distance[node] + i[1]
                visited[i[0]] = True

v = int(sys.stdin.readline())
graph = [[] for _ in range(v)]
max_idx = 0
distance = [0] * v
visited = [False] * v

for _ in range(v):
    v_num, *edges = map(int, sys.stdin.readline().split())
    for i in range(0, len(edges[:-1]), 2):
        graph[v_num - 1].append([edges[i] - 1, edges[i + 1]])

bfs(0, distance)
for i, d in enumerate(distance):
    if d > distance[max_idx]:
        max_idx = i

distance = [0] * v
visited = [False] * v

bfs(max_idx, distance)
print(max(distance))