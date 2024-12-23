import sys

n = int(sys.stdin.readline())
a = [0] * 100001
for i in range(n):
    a[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(a[i]):
        print(i)