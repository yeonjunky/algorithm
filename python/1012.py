import sys
from collections import deque


T = int(sys.stdin.readline().rstrip())
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = deque()

for _ in range(T):
    q.clear()
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    result = 0

    for _ in range(K):
        c, r = map(int, sys.stdin.readline().split())
        graph[r][c] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                result += 1
                q.append((i, j))
                visited[i][j] = 1

                while q:
                    r, c = q.popleft()

                    for d in DIRECTIONS:
                        new_r = r + d[0]
                        new_c = c + d[1]

                        if 0 <= new_r < N and 0 <= new_c < M:
                            if graph[new_r][new_c] and not visited[new_r][new_c]:
                                visited[new_r][new_c] = 1
                                q.append((new_r, new_c))

    print(result)
