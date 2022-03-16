import sys

n = int(sys.stdin.readline().replace('\n', ''))

arr = []
result = []

cnt = 1
m = 0
isError = False

for _ in range(n):
    num = int(sys.stdin.readline().replace('\n', ''))

    if m < num:
        for i in range(num - m):
            arr.append(cnt)
            result.append("+")
            cnt += 1
        m = num

    if arr[-1] == num:
        arr.pop()
        result.append("-")
    else:
        isError = True


if isError:
    print("NO")
else:
    for i in result:
        print(i)

