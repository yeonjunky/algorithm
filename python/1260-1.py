import sys
from collections import deque


def dfs(graph, visited, node):
    print(node, end=" ")
    for i in range(1, n + 1):
        if graph[node][i] and not visited[i - 1]:
            visited[i - 1] = True
            dfs(graph, visited, i)

def bfs(graph, visited, queue: deque):
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in range(1, n + 1):
            if graph[node][i] and not visited[i - 1]:
                visited[i - 1] = True
                queue.append(i)


n, m, v = map(int, sys.stdin.readline().split())
graph = [[False] * (n + 1) for _ in range(n + 1)] 
visited1 = [False] * n
visited2 = [False] * n
visited1[v - 1] = True
visited2[v - 1] = True
queue = deque([v])

for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1][v2] = True
    graph[v2][v1] = True

dfs(graph, visited1, v)
print()
bfs(graph, visited2, queue)