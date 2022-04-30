import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0 for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
queue = deque([])

for i in range(n):
    arr[i] = list(map(int, input().split()))

for i, sub_arr in enumerate(arr):
    for j, v in enumerate(sub_arr):
        if v == 2:
            queue.append([i, j])
            visited[i][j] = 1
            arr[i][j] = 0
        
        elif v == 1:
            arr[i][j] = -1

while queue:
    i, j = queue.popleft()

    for d in directions:
        row = i + d[0]
        col = j + d[1]

        if 0 <= row < n and 0 <= col < m:
            if not visited[row][col] and arr[row][col]:
                visited[row][col] = 1
                arr[row][col] = arr[i][j] + 1
                queue.append([row, col])

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print("")
