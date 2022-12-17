import sys

N, M = map(int, sys.stdin.readline().split())
MAX = 1000000001
nums = [0]
tree = [0] * (N * 4)

def init_tree(start, end, idx):
    global nums, tree
    if start == end:
        print(start, end, idx)
        tree[idx] = nums[start]
        return tree[idx]

    mid = (start + end) // 2

    tree[idx] = min(init_tree(start, mid, idx * 2), init_tree(mid + 1, end, idx * 2 + 1))
    return tree[idx]

def find_min(start, end, left, right, node):
    if left > end or right < start:
        return MAX
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(find_min(start, mid, left, right, node * 2), find_min(mid + 1, end, left, right, node * 2 + 1))


for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))
init_tree(1, N, 1)

for _ in range(M):
    l, r = map(int, sys.stdin.readline().split())
    prient(find_min(1, N, l, r, 1))
