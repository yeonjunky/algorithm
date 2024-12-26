import sys


def dfs(graph, visited, node, depth):
    global result
    if result or depth == 5:
        result = 1
        return

    for i in friend[node]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, visited, i, depth + 1)
            visited[i] = False


n, m = map(int, sys.stdin.readline().split())
friend = [[] for _ in range(n)]
visited = [False] * n
result = 0

for _ in range(m):
    p1, p2 = map(int, sys.stdin.readline().split())
    friend[p1].append(p2)
    friend[p2].append(p1)

for i in range(n):
    visited[i] = True
    dfs(friend, visited, i, 1)
    visited[i] = False

    if result:
        break

print(result)