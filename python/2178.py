import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
maze = []
queue = deque([(0, 0)])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[0] * m for _ in range(n)]

for _ in range(n):
    temp = []

    for i in sys.stdin.readline().rstrip():
        temp.append(int(i))

    maze.append(temp)

while queue:
    pos = queue.popleft()

    for d in directions:
        dy = pos[0] + d[0]
        dx = pos[1] + d[1]

        if 0 <= dx < m and 0 <= dy < n:
            if maze[dy][dx] and not visited[dy][dx]:
                queue.append([dy, dx])
                visited[dy][dx] = 1
                maze[dy][dx] = maze[pos[0]][pos[1]] + 1

print(maze[n - 1][m - 1])
