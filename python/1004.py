import sys

def is_inside(x, y, px, py, r):
    return (x - px) ** 2 + (y - py) ** 2 < r ** 2

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input().rstrip())
    cnt = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        contain_point = [is_inside(x1, y1, cx, cy, r), is_inside(x2, y2, cx, cy, r)]

        if (contain_point[0] and not contain_point[1]) or \
            (contain_point[1] and not contain_point[0]):
            cnt += 1

    print(cnt)
