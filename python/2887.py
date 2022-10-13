import sys


def find(n):
    if root[n] == n:
        return n
    root[n] = find(root[n])
    return root[n]

def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)

    if r1 != r2:
        if rank[r1] < rank[r2]:
            root[r1] = r2
        else:
            root[r2] = r1

        if rank[r1] == rank[r2]:
            rank[r1] += 1

def is_connected(n1, n2):
    return find(n1) == find(n2)

N = int(sys.stdin.readline())
planets = []
e = []
root = [i for i in range(N + 1)]
rank = [0] * (N + 1)
result = 0
e_cnt = 0

for i in range(N):
    planets.append([*map(int, sys.stdin.readline().split()), i])

for i in range(3):
    planets.sort(key=lambda p:p[i])
    previous = planets[0][3]

    for j in range(1, N):
        curr = planets[j][3]
        e.append([abs(planets[j][i] - planets[j - 1][i]), previous, curr])
        previous = curr


visited = [0] * N

e.sort(key=lambda a: a[0])
for d, s, e in e:
    if not is_connected(s, e):
        result += d
        union(s, e)
        e_cnt += 1

    if e_cnt == N - 1:
        break

print(result)
