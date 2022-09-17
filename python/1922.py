import sys


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
parent = [i for i in range(N + 1)]
visited = [0] * N
edges = []
cost = 0
edge_cnt = 0

def find_root(node):
    if parent[node] == node:
        return node
    parent[node] = find_root(parent[node])
    return parent[node]


def union(node1, node2):
    node1_root = find_root(node1)
    node2_root = find_root(node2)

    if node1_root != node2_root:
        parent[node2_root] = node1_root


def is_cycle(node1, node2):
    return find_root(node1) == find_root(node2)



for _ in range(M):
    edges.append(list(map(int, sys.stdin.readline().split())))

edges.sort(key= lambda e : e[2])

for e in edges:
    if find_root(e[0]) != find_root(e[1]):
        cost += e[2]
        edge_cnt += 1
        union(e[0], e[1])

        if edge_cnt == N - 1:
            break

print(cost)
