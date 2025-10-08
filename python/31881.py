import sys

n, Q = map(int, sys.stdin.readline().split())
com = [0] * n
cnt = n

for _ in range(Q):
    q = list(map(int, sys.stdin.readline().split()))

    if q[0] == 1:
        if com[q[1] - 1] == 0:
            cnt -= 1
        com[q[1] - 1] = 1
    elif q[0] == 2:
        if com[q[1] - 1] == 1:
            cnt += 1
        com[q[1] - 1] = 0
    else:
        print(cnt)
