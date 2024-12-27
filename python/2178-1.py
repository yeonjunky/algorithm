import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = []
move_cnt = [[0] * m for _ in range(n)]
directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
]
q = deque([[0, 0]])
move_cnt[0][0] = 1

for _ in range(n):
    maze.append(sys.stdin.readline().rstrip())

while q:
    node = q.popleft()

    for i in directions:
        ny = node[0] + i[0]
        nx = node[1] + i[1]
        if 0 <= ny < n and 0 <= nx < m \
            and maze[ny][nx] == '1' and not move_cnt[ny][nx]:
            move_cnt[ny][nx] = move_cnt[node[0]][node[1]] + 1
            q.append([ny, nx])

print(move_cnt[n - 1][m - 1])