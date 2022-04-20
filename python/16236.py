from collections import deque
import sys

input = sys.stdin.readline
level = 2
time = 0
ate_fish = 0
shark = [0, 0]
directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
fish_arr = []

n = int(input().rstrip())
arr = [0] * n
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))
    if max(arr[i]) == 9:
        shark = [0, i, arr[i].index(9)]
        arr[i][arr[i].index(9)] = 0

queue = deque([shark])

while True:
    while queue:
        d, x, y = queue.popleft()

        for d in directions:
            dx = d[0] + x
            dy = d[1] + y

            if 0 <= dy < n and 0 <= dx < n:
                if arr[dx][dy] <= level and not visited[dx][dy]:
                    visited[dx][dy] += visited[x][y] + 1
                    queue.append([visited[dx][dy], dx, dy])

                    if 0 < arr[dx][dy] < level:
                        fish_arr.append([visited[dx][dy], dx, dy])

    if fish_arr:
        fish_arr.sort()
        d, x, y = fish_arr[0]
        shark = [d, x, y]
        arr[x][y] = 0
        queue = deque([shark])
        time += visited[x][y]
        ate_fish += 1
        visited = [[0 for _ in range(n)] for _ in range(n)]
        fish_arr = []

        if ate_fish == level:
            level += 1
            ate_fish = 0

    else:
        break

print(time)
