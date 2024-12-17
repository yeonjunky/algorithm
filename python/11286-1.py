import sys
import heapq

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    op = int(sys.stdin.readline())

    if op:
        heapq.heappush(q, (abs(op), op))
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)