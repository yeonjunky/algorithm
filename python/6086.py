import sys

def dfs(graph):
    visited = []
    pass

n = int(sys.stdin.readline().rstrip())
graph = {}

for _ in range(n):
    v1, v2, c = sys.stdin.readline().split()
    c = int(c)

    if not graph.get(v1):
        graph[v1] = {}

    if not graph.get(v2):
        graph[v2] = {}

    graph[v1][v2] = c
    graph[v2][v1] = c

    