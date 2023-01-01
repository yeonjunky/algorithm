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
    melt = [[0] * M for _ in range(N)]

    while queue:
        r, c = queue.popleft()

        for d in D:
            nr, nc = r + d[0], c + d[1]

            if 0 <= nr < N and 0 <= nc < M:
                if not a[nr][nc]:
                    melt[r][c] -= 1
                    continue

                if not visited[nr][nc] and a[nr][nc]:
                    queue.append([nr, nc])
                    visited[nr][nc] = 1

    for i in range(N):
        for j in range(M):
            a[i][j] += melt[i][j]

for _ in range(N):
    a.append(list(map(int, sys.stdin.readline().split())))

while not exit:
    year += 1
    visited = [[0] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if a[i][j] and not visited[i][j]:
                bfs([i, j])
                cnt += 1

            if cnt >= 2:
                exit = True
                print(year)

            elif cnt == 0:
                exit = True
                print(0)
