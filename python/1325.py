import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
trust_com = {i: [] for i in range(n + 1)}
hackable_cnt = [0 for _ in range(n + 1)]
max_cnt = 0
dq = deque([])

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    trust_com[b].append(a)

for i in range(1, n + 1):
    dq.append(i)
    visited = [0 for _ in range(n + 1)]
    visited[i] = 1
    while dq:
        node = dq.popleft()
        hackable_cnt[i] += 1
        for j in trust_com[node]:
            if not visited[j]:
                dq.append(j)
                visited[j] = 1

    max_cnt = max(max_cnt, hackable_cnt[i])

for i in range(1, n + 1):
    if max_cnt == hackable_cnt[i]:
        sys.stdout.write(str(i) + ' ')