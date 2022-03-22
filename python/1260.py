from collections import deque
import sys

def dfs(graph, start, visited):
    visited[start - 1] = True

    print(start, end=' ')

    for i in graph[start]:
        if not visited[i - 1] and graph[start][0] != 0:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start - 1] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i - 1] and graph[start][0] != 0:
                queue.append(i)
                visited[i - 1] = True

n, m, v = map(int, sys.stdin.readline().split(' '))

graph =  [[0]] * (n + 1)
dfs_visited = [False] * n
bfs_visited = dfs_visited.copy()

for i in range(m):
    first, second = map(int, sys.stdin.readline().split(' '))
    
    if graph[first][0] == 0:
        graph[first] = []

    if graph[second][0] == 0:
        graph[second] = []

    if not first in graph[first]:
        graph[first].append(second)
        graph[second].append(first)

for i in graph:
    if i[0] != 0:
        i.sort()

print(graph)
dfs(graph, v, dfs_visited)
print('\n', end="")
bfs(graph, v, bfs_visited)
