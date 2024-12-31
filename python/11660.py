import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[0] * (n + 1)]

for i in range(n):
    arr.append([0] + list(map(int, sys.stdin.readline().split())))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

for _ in range(m):
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(arr[c][d] - (arr[c][b - 1] + arr[a - 1][d]) + arr[a - 1][b - 1])