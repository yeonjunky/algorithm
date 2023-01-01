import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
queue = deque()
a = []
exit = False
year = 0


def bfs(start):
    queue.append(start)

    while queue:
        r, c = queue.popleft()

        for d in D:
            nr, nc = r + d[0], c + d[1]

            if 0 <= nr < N and 0 <= nc < M:
                if a[nr][nc] == 0:
                    melt[r][c] -= 1
                    continue

                if not visited[nr][nc] and a[nr][nc]:
                    queue.append([nr, nc])
                    visited[nr][nc] = 1


for _ in range(N):
    a.append(list(map(int, sys.stdin.readline().split())))

while not exit:
    year += 1
    visited = [[0] * M for _ in range(N)]
    melt = [[0] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if a[i][j] and not visited[i][j]:
                bfs([i, j])
                cnt += 1

    for i in range(N):
        for j in range(M):
            val = a[i][j] + melt[i][j]
            a[i][j] = val if val >= 0 else 0

    if cnt >= 2:
        exit = True
        print(year)

    if cnt == 0:
        exit = True
        print(0)
