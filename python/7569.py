import sys
from collections import deque


M, N, H = map(int, sys.stdin.readline().split())
DIRECTIONS = [[1, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1]]

tomatoes = []
init_tomatoes = []
green_cnt = 0

for h in range(H):
    arr = []

    for r in range(N):
        temp = list(map(int, sys.stdin.readline().split()))

        for c in range(M):
            if temp[c] == 1:
                temp[c] = 1
                init_tomatoes.append((h, r, c))

            elif temp[c] == 0:
                green_cnt += 1

        arr.append(temp)

    tomatoes.append(arr)

queue = deque(init_tomatoes)

while queue:
    h, r, c = queue.popleft()

    for d in DIRECTIONS:
        n_h = h + d[0]
        row = r + d[1]
        col = c + d[2]

        if 0 <= n_h < H and 0 <= row < N and 0 <= col < M:
            if tomatoes[n_h][row][col] == 0:
                green_cnt -= 1
                tomatoes[n_h][row][col] = tomatoes[h][r][c] + 1
                queue.append((n_h, row, col))

if green_cnt:
    print(-1)

else:
    days = 0
    for i in range(H):
        for j in range(N):
            days = max([*tomatoes[i][j], days])

    print(days - 1)
