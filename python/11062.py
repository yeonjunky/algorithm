import sys
import heapq


N, M = map(int, sys.stdin.readline().split())
q = {i: [] for i in range(1, N + 1)}
q_cnt = [0] * N
pq = []
result = []

heapq.heapify(pq)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    q[a].append(b)
    q_cnt[b - 1] += 1

for i, v in enumerate(q_cnt):
    if v == 0:
        heapq.heappush(pq, i + 1)

for _ in range(N):
    v = heapq.heappop(pq)
    result.append(v)

    for i in q[v]:
        q_cnt[i - 1] -= 1

        if q_cnt[i - 1] == 0:
            heapq.heappush(pq, i)

print(*result)
