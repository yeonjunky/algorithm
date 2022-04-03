import sys
from collections import deque

directions = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]

while True:
    w, h = map(int, sys.stdin.readline().split())
    cnt = 0

    if not w and not h:
        break

    graph = [0 for i in range(h)]

    for i in range(h):
        graph[i] = list(map(int, sys.stdin.readline().split()))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                queue = deque([[i, j]])
                graph[i][j] = -1

                while queue:
                    pos = queue.popleft()

                    for d in directions:
                        row = pos[0] + d[0]
                        col = pos[1] + d[1]

                        if not 0 <= row < h or not 0 <= col < w:
                            continue

                        elif graph[row][col] == 1:
                            graph[row][col] = -1
                            queue.append([row, col])

                cnt += 1

    print(cnt)

