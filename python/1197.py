import sys


V, E = map(int, sys.stdin.readline().split())
parent = [i for i in range(V + 1)]
edges = []
cost = 0
edge_cnt = 0


def union(node1, node2):
    node1_root = find_root(node1)
    node2_root = find_root(node2)

    if node1_root != node2_root:
        parent[node2_root] = node1_root


def find_root(node):
    if parent[node] == node:
        return node
    parent[node] = find_root(parent[node])
    return parent[node]


def is_cycle(node1, node2):
    return find_root(node1) == find_root(node2)

for _ in range(E):
    edges.append(list(map(int, sys.stdin.readline().split())))

edges.sort(key=lambda e : e[2])

for e in edges:
    if not is_cycle(e[0], e[1]):
        cost += e[2]
        edge_cnt += 1
        union(e[0], e[1])

        if edge_cnt == V - 1:
            break

print(cost)
