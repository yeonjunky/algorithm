import sys

n, m = map(int, sys.stdin.readline().split(' '))
pos = list(map(int, sys.stdin.readline().split(' ')))
cnt = 0

def move_right(val):
    if val + 1 > n:
        return 1
    else:
        return val + 1

def move_left(val):
    if val - 1 < 1:
        return n
    else:
        return val - 1


for i in range(m):
    target = pos.pop(0) - 1 # switch position to index

    if target <= (n-1)/2:
        cnt += target
        for j in range(target + 1):
            pos = list(map(move_left, pos))
        
    else:
        cnt += n - target 
        for j in range(n - target):
            pos = list(map(move_right, pos))
        pos = list(map(move_left, pos))

    n -= 1

print(cnt)