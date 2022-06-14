import sys


x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())

v1 = [x2 - x1, y2 - y1]
v2 = [x3 - x1, y3 - y1]

# vector cross product
cp = v1[0] * v2[1] - v1[1] * v2[0]

if cp == 0:
    print(0)

elif cp < 0:
    print(-1)

else:
    print(1)
