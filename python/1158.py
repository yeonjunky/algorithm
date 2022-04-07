import sys
from collections import deque

input = sys.stdin.readline
queue = []

n, k = map(int, input().split())
arr = deque(list(range(1, n + 1)))

while arr:
    for _ in range(k - 1):
        arr.append(arr.popleft())

    queue.append(arr.popleft())

print(str(queue).replace('[', '<').replace(']', '>'))
