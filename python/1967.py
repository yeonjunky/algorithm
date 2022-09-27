'''
####### 정해는 따로 있음(1967-1.py)#######
idea: 리프 노드를 구해서
      모든 리프노드에서 BFS
      이떄 최대값이 결과
'''

import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())
e = {}
max_cost = 0
leaf_node = []
global_visited = [0] * (N + 1)
queue = deque()

for _ in range(N - 1):
    p, c, w = map(int, sys.stdin.readline().split())
    if p not in e:
        e[p] = [(c, w)]
    else:
        e[p].append((c, w))

    if c not in e:
        e[c] = [(p, w)]
    else:
        e[c].append((p, w))

for i in e.keys():
    if len(e[i]) == 1:
        leaf_node.append(i)

for l in leaf_node:
    visited = [0] * (N + 1)
    visited[l] = 1

    for idx, gv in enumerate(global_visited):
        if gv:
            visited[idx] = 1

    queue.clear()
    queue.append((l, 0))

    while queue:
        v = queue.popleft()
        max_cost = max(max_cost, v[1])

        for i in e[v[0]]:
            if not visited[i[0]]:
                visited[i[0]] = 1
                queue.append((i[0], v[1] + i[1]))

    global_visited[l] = 1

print(max_cost)
