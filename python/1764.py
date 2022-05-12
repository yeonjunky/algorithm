import sys

input = sys.stdin.readline
not_listen = {}
not_see = {}
result = []

n, m = map(int, input().split())

for _ in range(n):
    name = input().rstrip()
    not_listen[name] = 0

for _ in range(m):
    name = input().rstrip()
    not_see[name] = 1

for i in not_listen.keys():
    if i in not_see:
        result.append(i)

print(len(result))
result.sort()
for i in result:
    print(i)
