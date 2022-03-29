import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split(' '))
graph = []
red = []
green_cnt = 0
cnt = 0
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for i in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if li[j] == 1:
            red.append([i, j])
        elif li[j] == 0:
            green_cnt += 1
    graph.append(li)

if green_cnt == 0:
    print(0)

else:
    queue = deque(red)

    while queue:
        v = queue.popleft()

        for dir in direction:
            row = v[0] + dir[0]
            col = v[1] + dir[1]

            if row < 0 or row > n - 1 or col < 0 or col > m - 1:
                pass

            elif graph[row][col] == 0:
                graph[row][col] = graph[v[0]][v[1]] + 1
                green_cnt -= 1
                queue.append([row, col])
            
                if cnt < graph[row][col]:
                    cnt = graph[row][col]

    if green_cnt:
        print(-1)
    else:
        print(cnt - 1)