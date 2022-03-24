import sys
from collections import deque

t = int(sys.stdin.readline().replace('\n', ''))

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split(' '))
    queue = deque(list(map(int, sys.stdin.readline().split(' '))))

    obj_val = queue[m]
    current_idx = m
    cnt = 1

    while True:
        highest = max(queue)

        if current_idx < 0:
            current_idx = len(queue) - 1

        if highest == obj_val and current_idx == 0:
            print(cnt)
            break

        elif queue[0] == highest:
            queue.popleft()
            current_idx -= 1
            cnt += 1

        elif queue[0] != highest:
            v = queue.popleft()
            queue.append(v)
            current_idx -= 1
