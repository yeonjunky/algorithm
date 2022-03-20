import sys

n = int(sys.stdin.readline().replace('\n', ''))
stack = []
cnt = 0

for _ in range(n):
    level = int(sys.stdin.readline().replace('\n', ''))

    if len(stack) > 0:
        while stack[-1] <= level:
            stack.pop()

            if len(stack) == 0:
                break

        cnt += len(stack)

    stack.append(level)

print(cnt)