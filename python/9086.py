import sys
l = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
	l.append(sys.stdin.readline().rstrip())
for i in range(n):
	print(l[i][0] + l[i][-1])