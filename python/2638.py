import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
arr = []
is_complete = False
directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]

cheese_num = 0
days = 0

for _ in range(n):
    sub_arr = list(map(int, sys.stdin.readline().split()))

    for i in sub_arr:
        if i == 1:
            cheese_num += 1

    arr.append(sub_arr)

while cheese_num > 0:
    queue = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    cheese = []

    while queue:
        v = queue.popleft()

        for d in directions:
            row = v[0] + d[0]
            col = v[1] + d[1]

            if 0 <= row < n and 0 <= col < m:
                if arr[row][col] == 0 and not visited[row][col]:
                    visited[row][col] = 1
                    queue.append((row, col))

                elif arr[row][col]:
                    arr[row][col] += 1
                    if (row, col) not in cheese:
                        cheese.append((row, col))

    for r, c in cheese:
        if arr[r][c] > 2:
            cheese_num -= 1
            arr[r][c] = 0

        else:
            arr[r][c] = 1

    days += 1

print(days)
