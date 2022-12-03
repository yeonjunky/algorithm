import sys
from collections import deque


M, N = map(int, sys.stdin.readline().split())
maze = []
w = [[0] * M for _ in range(N)]

for _ in range(N):
	t = []
	for i in sys.stdin.readline():
		t.append(i)
	maze.append(t)

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
q = deque([[0, 0]])
maze[0][0] = -1

while q:
	curr = q.popleft()

	for d in DIR:
		r = curr[0] + d[0]
		c = curr[1] + d[1]

		if 0 <= r < N and 0 <= c < M:
			if maze[r][c] == "0":
				w[r][c] = w[curr[0]][curr[1]]
				q.appendleft([r, c])

			elif maze[r][c] == "1":
				w[r][c] = w[curr[0]][curr[1]] + 1
				q.append([r, c])

			maze[r][c] = -1

print(w[N - 1][M - 1])
