'''
idea: 기본적인 union and find 문제
      친구 관계를 입력받으면 두 노드를 union
      두 사람 사이에 관계가 있는지를 찾으려면
      root를 찾아 같으면 1, 다르면 0을 출력한다.
'''

import sys


def find_root(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find_root(parent, parent[node])
    return parent[node]


def union(parent, node1, node2):
    node1_root = find_root(parent, node1)
    node2_root = find_root(parent, node2)

    if node1_root != node2_root:
        parent[node2_root] = node1_root


T = int(sys.stdin.readline().rstrip())

for t in range(1, T + 1):
    N = int(sys.stdin.readline().rstrip())
    K = int(sys.stdin.readline().rstrip())

    parent = list(range(N))
    friend = []

    for _ in range(K):
        users = list(map(int, sys.stdin.readline().split()))

        union(parent, users[0], users[1])

    M = int(sys.stdin.readline().rstrip())

    for i in range(M):
        friend.append(list(map(int, sys.stdin.readline().split())))

    print(f'Scenario {t}:')
    for f in friend:
        if find_root(parent, f[0]) == find_root(parent, f[1]):
            print(1)
        else:
            print(0)

    print()
    