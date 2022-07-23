import sys


n, m = map(int, sys.stdin.readline().split())

title = []

for _ in range(n):
    t = sys.stdin.readline().split()
    t[1] = int(t[1])
    title.append(t)

for _ in range(m):
    val = int(sys.stdin.readline().rstrip())
    left = 0
    right = len(title) - 1

    while(left < right):
        mid = (left + right) // 2
        
        if val <= title[mid][1]:
            right = mid

        else:
            left = mid + 1

    print(title[left][0])