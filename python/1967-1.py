'''
####### 정해 #######
idea: 임의의 노드 x에서 가장 먼 거리에 있는 노드 a 탐색
      a에서 가장 먼 거리에 있는 노드 b 탐색
      a와 b를 연결하는 경로가 트리의 지름
'''
import sys
sys.setrecursionlimit(1000000000)


def dfs(num, curr_cost):
    for i in e[num]:
        if distance[i[0]] == -1:
            distance[i[0]] = curr_cost + i[1]
            dfs(i[0], curr_cost + i[1])


N = int(sys.stdin.readline().rstrip())
e = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    e[a].append([b, c])
    e[b].append([a, c])

distance = [-1] * (N + 1)
distance[1] = 0
dfs(1, 0)

end = distance.index(max(distance))
distance = [-1] * (N + 1)
distance[end] = 0

dfs(end, 0)

print(max(distance))
