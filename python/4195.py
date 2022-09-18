'''
idea: 유저가 문자열로 주어지기 때문에 dict 사용
      {user: [root_user, 자신 포함 union 과정에서 자신에게 연결되는 집합의 유저 수]}
      union 때 마다 루트 노드의 집합 유저 수 출력

'''

import sys


def find_root(parent, node):
    if parent[node][0] == node:
        return node
    parent[node][0] = find_root(parent, parent[node][0])
    return parent[node][0]

def union(parent, node1, node2):
    node1_root = find_root(parent, node1)
    node2_root = find_root(parent, node2)

    if node1_root != node2_root:
        parent[node2_root][0] = node1_root
        parent[node1_root][1] += parent[node2_root][1]


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    F = int(sys.stdin.readline().rstrip())
    parent = {}

    for _ in range(F):
        users = sys.stdin.readline().split()

        for u in users:
            if u not in parent:
                parent[u] = [u, 1]

        union(parent, users[0], users[1])

        print(parent[find_root(parent, users[0])][1])
