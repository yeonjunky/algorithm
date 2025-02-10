import sys


def init(tree, a, start, end, node):
    if start == end:
        tree[node] = a[start]
        return tree[node]

    mid = (start + end) // 2
    l = init(tree, a, start, mid, node * 2)
    r = init(tree, a, mid + 1, end, node * 2 + 1)
    tree[node] = l * r % 1000000007
    return tree[node]

def update(tree, origin, new, node, start, end, arr_idx):
    if not (start <= arr_idx <= end): return

    if start == end: 
        tree[node] = new
        return
    mid = (start + end) // 2
    update(tree, origin, new, node * 2, start, mid, arr_idx)
    update(tree, origin, new, node * 2 + 1, mid + 1, end, arr_idx)
    tree[node] = tree[node * 2] * tree[node * 2 + 1] % 1000000007

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 1
    
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    l = query(tree, node * 2, start, mid, left, right)
    r = query(tree, node * 2 + 1, mid + 1, end, left, right)
    return l * r % 1000000007

n, m, k = map(int, sys.stdin.readline().split())
arr = []
tree = [0] * (n * 4)

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

init(tree, arr, 0, n - 1, 1)

for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        update(tree, arr[b - 1], c, 1, 0, n - 1, b - 1)
    elif a == 2:
        print(query(tree, 1, 0, n - 1, b - 1, c - 1))
