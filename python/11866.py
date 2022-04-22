import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque(list(range(1, n + 1)))
result = []

while queue:
    for _ in range(1, k):
        v = queue.popleft()
        queue.append(v)

    v = queue.popleft()
    result.append(v)

print('<', end='')
for i in range(n - 1):
    print(result[i], end=', ')

print(result[n - 1], end='>')