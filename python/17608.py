import sys

n = int(input())

cnt = 0
high = 0

arr = [int(sys.stdin.readline()) for _ in range(n)]

while arr:
    element = arr.pop()
    if element > high:
        high = element
        cnt += 1

print(cnt)
