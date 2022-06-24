import sys
import heapq


INF = int(1e9)

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline().rstrip())
edge = [[] for _ in range(v + 1)]
min_cost = [INF] * v
queue = []

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())

    edge[u].append((v, w))

heapq.heappush(queue, (0, k))
min_cost[k - 1] = 0

while queue:
    c, v = heapq.heappop(queue)

    if min_cost[v - 1] < c:
        continue

    for i in edge[v]:
        cost = min_cost[v - 1] + i[1]

        if cost < min_cost[i[0] - 1]:
            min_cost[i[0] - 1] = cost
            heapq.heappush(queue, (cost, i[0]))

for i in min_cost:
    if i == INF:
        print('INF')
    else:
        print(i)
