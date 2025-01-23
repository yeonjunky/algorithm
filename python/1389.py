import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[105] * n for _ in range(n)]
result = -1
min_val = sys.maxsize

for i in range(n):
	graph[i][i] = 0

for _ in range(m):
	a, b = map(int, sys.stdin.readline().split())
	graph[a - 1][b - 1] = 1
	graph[b - 1][a - 1] = 1

for k in range(n):
	for i in range(n):
		for j in range(n):
			if graph[i][j] > graph[i][k] + graph[k][j]:
				graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
	s = sum(graph[i])
	if min_val > s:
		result = i + 1
		min_val = s

print(result)