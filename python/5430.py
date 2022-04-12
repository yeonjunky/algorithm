import sys
from collections import deque

input = sys.stdin.readline
t = int(input().rstrip())

for _ in range(t):
    p = input().rstrip()
    n = int(input().rstrip())
    arr = input().rstrip().replace('[', '').replace(']', '')
    isReverse = False
    isError = False

    if arr:
        arr = list(map(int, arr.split(',')))

    if not isError:
        queue = deque(arr)

        for i in p:
            if i == "R":
                isReverse = not isReverse

            else:
                if len(queue):
                    if isReverse:
                        queue.pop()
                    else:
                        queue.popleft()
                else:
                    isError = True
                    break

    if isError:
        print("error")
    else:
        print('[', end='')
        if isReverse:
            queue.reverse()
        
        while queue:
            if len(queue) == 1:
                print(queue.popleft(), end='')
            else:
                print(queue.popleft(), end=',')
        print(']')