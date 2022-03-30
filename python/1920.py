import sys

n = int(sys.stdin.readline().replace('\n', ''))
a = list(map(int, sys.stdin.readline().split()))
a.sort()

n = int(sys.stdin.readline().replace('\n', ''))
b = list(map(int, sys.stdin.readline().split()))

for i in b:
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if i < a[mid]:
            right = mid - 1
        elif i > a[mid]:
            left = mid + 1
        else:
            break

    if i == a[mid]:
        print(1)
    else:
        print(0)

