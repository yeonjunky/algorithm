import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
place = [0 for i in range(n)]
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
turn_cnt = 0
cnt = 1

for i in range(n):
    place[i] = list(map(int, input().split()))

while True:
    place[r][c] = -1
    temp = [r, c]

    for i in range(4):
        d += 3
        if place[r + direction[d % 4][0]][c + direction[d % 4][1]] == 0:
            r += direction[d % 4][0]
            c += direction[d % 4][1]
            cnt += 1
            break

    if temp == [r, c]:
        if place[r + direction[(d + 2) % 4][0]][c + direction[(d + 2) % 4][1]] != 1:
            r += direction[(d + 2) % 4][0]
            c += direction[(d + 2) % 4][1]

        elif turn_cnt == 4:
            break

        else:
            turn_cnt += 1

print(cnt)
