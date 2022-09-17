import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())
graph = []
visited = [[0] * N for _ in range(N)]
queue = deque()
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
building_complex = []

for _ in range(N):
    graph.append(sys.stdin.readline().rstrip())

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and not visited[i][j]:
            queue.append((i, j))
            visited[i][j] = 1
            cnt = 1

            while queue:
                r, c = queue.popleft()

                for d in DIRECTIONS:
                    new_r = r + d[0]
                    new_c = c + d[1]

                    if 0 <= new_r < N and 0 <= new_c < N:
                        if graph[new_r][new_c] == '1' and not visited[new_r][new_c]:
                            queue.append((new_r, new_c))
                            visited[new_r][new_c] = 1
                            cnt += 1
                        
            building_complex.append(cnt)

building_complex.sort()

print(len(building_complex))

for b in building_complex:
    print(b)
