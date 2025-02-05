import sys

n = int(sys.stdin.readline())
graph = []
result = [[105] * n for _ in range(n)]

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if a[j] == 0:
            a[j] = 105
    graph.append(a)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    for j in range(n):
        print(1 if 105 > graph[i][j] > 0 else 0, end=' ')
    print()