import sys

def dfs(graph, n, visited):
    visited[n] = 1

    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)

c = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

graph = {}
for i in range(1, c + 1):
    graph[i] = []
visited = [0 for i in range(c + 1)]
result = 0

for _ in range(n):
    l, r = map(int, sys.stdin.readline().split())
    graph[l].append(r)
    graph[r].append(l)

dfs(graph, 1, visited)

for i in visited:
    if i:
        result += 1

print(result - 1)
