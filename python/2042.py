import sys
import math

N, M, K = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

tree = [0] * (2 * (2 ** math.ceil(math.log(N, 2))) - 1)

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]

    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

def update(s, e, i, origin, new, arr_idx):
    if not s <= arr_idx <= e: return

    tree[i] += new - origin

    if s == e: return
    m = (s + e) // 2
    update(s, m, i * 2, origin, new, arr_idx)
    update(m + 1, e, i * 2 + 1, origin, new, arr_idx)

def query(start, end, index, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[index]

    mid = (start + end) // 2
    return query(start, mid, index * 2, left, right) + query(mid + 1, end, index * 2 + 1, left, right)


init(0, N - 1, 1)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        update(0, N - 1, 1, arr[b-1], c, b-1)
        arr[b-1] = c
    else:
        print(query(0, N - 1, 1, b - 1, c - 1))


