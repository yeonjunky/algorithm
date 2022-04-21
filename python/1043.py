import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
init_truth = list(map(int, input()[1:].split()))
know_truth = [0] * (n + 1)
cnt = 0
party = []
graph = dict([(i, [i]) for i in range(1, n + 1)])
queue = deque(init_truth)

for i in range(m):
    arr = input().split()
    party.append(list(map(int, arr[1:])))

    if arr[0] != 1:
        for val in party[i]:
            temp = list(set(party[i]) - set(graph[val]))
            graph[val].extend(temp)

for i in graph.items():
    graph[i[0]] = i[1][1:]
    
for i in init_truth:
    know_truth[i] = 1

while queue:
    v = queue.popleft()

    for i in graph[v]:
        if not know_truth[i]:
            know_truth[i] = 1
            queue.append(i)

for i in range(m):
    for j in party[i]:
        if know_truth[j]:
            break

        elif party[i][len(party[i]) - 1] == j and not know_truth[j]:
            cnt += 1

print(cnt)
