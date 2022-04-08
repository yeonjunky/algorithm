import sys

n = int(sys.stdin.readline().replace('\n', ''))
a = list(map(int, sys.stdin.readline().split()))

stack = []
result = [-1] * n

for i, v in enumerate(a):
    if not stack:
        stack.append(i)

    else:
        length = len(stack)

        while v > a[stack[length - 1]]:
            result[stack.pop()] = v
            length -= 1
            if not length:
                break

        stack.append(i)

for i in range(n):
    print(result[i], end=' ')
