import sys

N, Q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
tree = [0] * (N * 4)

def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
        return tree[node]

def interval_sum(start, end, idx, left, right):
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[idx]

    mid = (start + end) // 2
    return interval_sum(start, mid, idx * 2, left, right) + interval_sum(mid + 1, end, idx * 2 + 1, left, right)

def update(start, end, idx, change_node, diff):
    if change_node < start or change_node > end:
        return

    tree[idx] += diff

    if start != end:
        mid = (start + end) // 2
        update(start, mid, idx * 2, change_node, diff)
        update(mid + 1, end, idx * 2 + 1, change_node, diff)

init(0, N - 1, 1)

for _ in range(Q):
    x, y, a, b = map(int, sys.stdin.readline().split())

    x, y = x - 1, y - 1
    a -= 1

    if x > y:
        x, y = y , x

    print(interval_sum(0, N - 1, 1, x, y))
    update(0, N - 1, 1, a, b - arr[a])
    arr[a] = b
    print(tree)
