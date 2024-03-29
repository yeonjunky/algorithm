import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque([])

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(int(command[1]))

    elif command[0] == 'pop':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(queue))

    elif command[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
