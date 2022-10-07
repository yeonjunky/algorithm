import sys


def union(n1, n2):
    n1_root = find(n1)
    n2_root = find(n2)
    if n1_root != n2_root:
        city_root[n2_root] = n1_root

def find(n):
    if city_root[n] == n:
        return n
    city_root[n] = find(city_root[n])
    return city_root[n]

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

city_root = [*range(N + 1)]

for i in range(1, N + 1):
    e = list(map(int, sys.stdin.readline().split()))
    for j, v in enumerate(e):
        if v:
            union(i, j + 1)
    
plan = list(map(int, sys.stdin.readline().split()))
is_possible = True

for i in range(1, M):
    if find(plan[i]) != find(plan[i - 1]):
        is_possible = False
        break

if is_possible:
    print("YES")
else:
    print("NO")
