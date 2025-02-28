p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

v1 = [p1[0] - p2[0], p1[1] - p2[1]]
v2 = [p2[0] - p3[0], p2[1] - p3[1]]

cp = v1[0] * v2[1] - v1[1] * v2[0]

if (0 < cp): print(1)
elif (cp < 0): print(-1)
else: print(0)