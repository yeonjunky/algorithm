import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
LAB = []
temp = [[0] * M for _ in range(N)]


def virus():
    queue = deque(v_pos)

    while queue:
        r, c = queue.popleft()

        for d in DIRECTIONS:
            row = r + d[0]
            col = c + d[1]

            if 0 <= row < N and 0 <= col < M:
                if temp[row][col] == 0:
                    temp[row][col] = 2
                    queue.append((row, col))

def get_safearea():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                cnt += 1
    return cnt

def build_wall(cnt):
    global result

    if cnt == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = LAB[i][j]

        virus()

        result = max(result, get_safearea())


    else:
        for i in range(N):
            for j in range(M):
                if LAB[i][j] == 0:
                    LAB[i][j] = 1
                    build_wall(cnt + 1)
                    LAB[i][j] = 0


v_pos = [] # virus position
result = 0

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))

    for j in range(M):
        if arr[j] == 2:
            v_pos.append((i, j))

    LAB.append(arr)

build_wall(0)

print(result)
