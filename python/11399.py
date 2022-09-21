import sys


N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))
sum = 0
result = 0

P.sort()

for i in range(N):
    sum += P[i]
    result += sum

print(result)
