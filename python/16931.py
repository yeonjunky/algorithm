import sys

n, m = map(int, sys.stdin.readline().split())
shape = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
surface_area = 0

for i in range(n):
    for j in range(1, m):
        if shape[i][j] > shape[i][j - 1]:
            surface_area += shape[i][j] - shape[i][j - 1]

for i in range(m):
    for j in range(1, n):
        if shape[j][i] > shape[j - 1][i]:
            surface_area += shape[j][i] - shape[j - 1][i]

for i in range(n):
    surface_area += shape[i][0]

for j in range(m):
    surface_area += shape[0][j]

surface_area *= 2 # 앞, 옆면 한 쪽씩만 넓이를 구하고, surface_area * 2
surface_area += 2 * n * m # 빈 칸은 없기 때문에 윗, 아랫면은 무조건 n * m

print(surface_area)
