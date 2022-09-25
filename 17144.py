import sys
from copy import deepcopy


R, C, T = map(int, sys.stdin.readline().split())
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
room = []
air_purifier = []

for r in range(R):
    col = list(map(int, sys.stdin.readline().split()))

    for c in col:
        if c == -1:
            air_purifier.append(r)
    room.append(col)

for _ in range(T):
    new_room = deepcopy(room)
    for r in range(R):
        for c in range(C):
            if room[r][c] > 1:
                new_val = room[r][c] // 5
                cnt = 0

                for d in DIR:
                    new_r = r + d[0]
                    new_c = c + d[1]

                    if 0 <= new_r < R and 0 <= new_c < C:
                        if room[new_r][new_c] > -1:
                            new_room[new_r][new_c] += new_val
                            new_room[r][c] -= new_val

    room = new_room

    for i in range(2):
        r = air_purifier[i]
        c = 0
        previous = 0

        if i == 0:
            while c < C - 1:
                c += 1
                room[r][c], previous = previous, room[r][c]

            while 0 < r:
                r -= 1
                room[r][c], previous = previous, room[r][c]

            while 0 < c:
                c -= 1
                room[r][c], previous = previous, room[r][c]

            while r < air_purifier[i] - 1:
                r += 1
                room[r][c], previous = previous, room[r][c]

        else:
            while c < C - 1:
                c += 1
                room[r][c], previous = previous, room[r][c]

            while r < R - 1:
                r += 1
                room[r][c], previous = previous, room[r][c]

            while 0 < c:
                c -= 1
                room[r][c], previous = previous, room[r][c]

            while air_purifier[i] < r - 1:
                r -= 1
                room[r][c], previous = previous, room[r][c]

sum = 0

for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            sum += room[i][j]
print(sum)