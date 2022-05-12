import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
cranes = deque(sorted(list(map(int, input().split())), reverse=True))
m = int(input().rstrip())
boxes = deque(sorted(list(map(int, input().split())), reverse=True))
time = 0

if cranes[0] < boxes[0]:
    print(-1)

else:
    for _ in range(len(cranes)):
        if cranes[n - 1] < boxes[m - 1]:
            cranes.pop()
            n -= 1
        
        else:
            break

    while boxes:
        time += 1

        for i in cranes:
            if not boxes:
                break
            for j in boxes:
                if i >= j:
                    boxes.remove(j)
                    break

    print(time)
