import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())
friend = [[] for _ in range(n + 1)]
result = 1
queue = deque()
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(1, n + 1):
    distance = [0] * (n + 1)
    queue.append(i)

    while queue:
        node = queue.popleft()
        for j in friend[node]:
            if not distance[j]:
                queue.append(j)
                distance[j] = distance[node] + 1
                if distance[j] > 6:
                    result = 0

    for j in distance[1:]:
        if j == 0:
            result = 0 

    if not result:
        break; 

print("Small World!" if result else "Big World!")