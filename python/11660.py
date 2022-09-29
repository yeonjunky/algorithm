import sys


N, M = map(int, sys.stdin.readline().split())
arr = [[0] * (N + 1)]

for _ in range(N):
    arr.append([0] + list(map(int, sys.stdin.readline().split())))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

for _ in range(M):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    print(arr[y2][x2] - (arr[y2][x1 - 1] + arr[y1 - 1][x2]) + arr[y1 - 1][x1 - 1])
