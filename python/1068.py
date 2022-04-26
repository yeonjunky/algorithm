import sys

sys.setrecursionlimit(2000)

n = int(sys.stdin.readline().rstrip())
tree = {}
tree[-1] = []
for i in range(n):
    tree[i] = []
leaf_node = 0

def dfs(tree, node):
    global leaf_node

    if node in tree:
        if tree[node]:
            for i in tree[node]:
                dfs(tree, i)

        elif node != -1:
            leaf_node += 1

parents = list(map(int, sys.stdin.readline().split()))

for i, v in enumerate(parents):
    tree[v].append(i)

del_node = int(sys.stdin.readline().rstrip())
tree.pop(del_node)

for i in tree.values():
    if del_node in i:
        i.pop(i.index(del_node))

dfs(tree, -1)
print(leaf_node)
