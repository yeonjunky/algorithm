import sys
from collections import deque


A = []
N, L, R = map(int, sys.stdin.readline().split())
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

days = 0
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

while True:
    is_migration = False
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                need_search = False

                for d in directions:
                    row = i + d[0]
                    col = j + d[1]

                    if not (0 <= row < N and 0 <= col < N):
                            continue

                    if not visited[row][col] and L <= abs(A[row][col] - A[i][j]) <= R:
                        need_search = True

                if need_search:
                    union = [(i, j)]
                    u_population = A[i][j]

                    queue = deque([(i, j)])
                    visited[i][j] = True

                    while queue:
                        v = queue.popleft()

                        for d in directions:
                            row = v[0] + d[0]
                            col = v[1] + d[1]

                            if not (0 <= row < N and 0 <= col < N):
                                continue
                            
                            if not visited[row][col] and L <= abs(A[row][col] - A[v[0]][v[1]]) <= R:
                                is_migration = True
                                visited[row][col] = True
                                queue.append((row, col))
                                union.append((row, col))
                                u_population += A[row][col]

                    new_population = u_population // len(union)

                    for a in union:
                        A[a[0]][a[1]] = new_population

    if is_migration:
        is_migration = False
        days += 1

    else:
        break

print(days)