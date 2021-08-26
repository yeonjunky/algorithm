import sys

li = []

k = int(sys.stdin.readline())

for _ in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        li.append(num)
    else:
        li.pop(-1)

print(sum(li))