import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
dq = deque()

for i in range(n):
    while dq and a[i] <= dq[-1][0]:
        dq.pop()
    dq.append([a[i], i])
    while i - l + 1 > dq[0][1]:
        node = dq.popleft()
    sys.stdout.write(str(dq[0][0]) + ' ')