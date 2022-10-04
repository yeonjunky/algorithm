import sys
import heapq as h


N = int(sys.stdin.readline())
hq = []
days = [0] * 10000
result = 0

for _ in range(N):
    p, d = map(int, sys.stdin.readline().split())
    h.heappush(hq, (-p, d))

for _ in range(N):
    p, d = h.heappop(hq)
    i = d - 1
    
    while i >= 0:
        if not days[i]:
            result += -p
            days[i] = 1
            break
        i -= 1

print(result)
