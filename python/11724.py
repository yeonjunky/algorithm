import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start - 1] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i - 1]:
                queue.append(i)
                visited[i - 1] = True


n, m = map(int, sys.stdin.readline().split())
g = {}
visited = [False] * n
cnt = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if not u in g:
        g[u] = [v]
    else:
        g[u].append(v)
    if not v in g:
        g[v] = [u]
    else:
        g[v].append(u)

for i in range(1, n + 1):
    if not i in g:
        cnt += 1
        continue

    if not visited[i - 1]:
        bfs(g, i, visited)
        cnt += 1

print(cnt)