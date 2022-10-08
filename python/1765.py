import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
root = [*range(N + 1)]
e = {i: [] for i in range(1, N + 1)}
team_cnt = N

def union(n1, n2):
    global team_cnt
    n1_root = find(n1)
    n2_root = find(n2)

    if n1_root != n2_root:
        root[n2_root] = n1_root
        team_cnt -= 1

def find(n):
    if root[n] == n:
        return n
    root[n] = find(root[n])
    return root[n]

for _ in range(M):
    r, p, q = sys.stdin.readline().split()
    p, q = int(p), int(q)
    if r == 'F':
        union(p, q)

    else:
        e[p].append(q)
        e[q].append(p)
        union(e[p][0], e[p][-1])
        union(e[q][0], e[q][-1])

print(team_cnt)
