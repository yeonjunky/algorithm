import sys
from collections import deque    

input = sys.stdin.readline

n = int(input().rstrip())
paint = []
non_CBlind = 0
CBlind = 0
queue = deque([])
v = [[0 for _ in range(0, n)] for _ in range(0, n)]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for _ in range(n):
    paint.append(list(input().rstrip()))

for i in range(n):
    for j in range(n):
        curr = paint[i][j]

        if v[i][j]:
            continue
        else:
            queue.append([i, j])
            v[i][j] = 1

        while queue:
            x, y = queue.popleft()

            for d in dir:
                dx = x + d[0]
                dy = y + d[1]

                if 0 <= dx < n and 0 <= dy < n:
                    if paint[dx][dy] == curr and not v[dx][dy]:
                        queue.append([dx, dy])
                        v[dx][dy] = 1

            if not queue:
                non_CBlind += 1
                break

for i in range(n):
    new_val = ''
    for j in range(n):
        v[i][j] = 0
        if paint[i][j] == 'G':
            paint[i][j] = 'R'
        
queue = deque()

for i in range(n):
    for j in range(n):
        curr = paint[i][j]

        if v[i][j]:
            continue
        else:
            queue.append([i, j])
            v[i][j] = 1

        while queue:
            x, y = queue.popleft()

            for d in dir:
                dx = x + d[0]
                dy = y + d[1]

                if 0 <= dx < n and 0 <= dy < n:
                    if paint[dx][dy] == curr and not v[dx][dy]:
                        queue.append([dx, dy])
                        v[dx][dy] = 1

            if not queue:
                CBlind += 1
                break

print(non_CBlind, CBlind)
