import sys


N, M = map(int, sys.stdin.readline().split())
name_id = {}
id_name = {}

for i in range(1, N + 1):
    name = sys.stdin.readline().rstrip()
    name_id[name] = i
    id_name[i] = name

for i in range(M):
    name = sys.stdin.readline().rstrip()

    if 49 <= ord(name[0]) <= 57:
        print(id_name[int(name)])
    else:
        print(name_id[name])
