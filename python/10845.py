import sys
from collections import deque

n = int(sys.stdin.readline().replace('\n', ''))
size = 0
queue = deque()

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(int(command[1]))
        size += 1

    elif command[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            print(queue.popleft())
            size -= 1
    
    elif command[0] == 'size':
        print(size)

    elif command[0] == 'empty':
        print(int(size == 0))

    elif command[0] == 'front':
        if size == 0:
            print(-1)
        else:
            print(queue[0])

    else:
        if size == 0:
            print(-1)
        else:
            print(queue[size - 1])