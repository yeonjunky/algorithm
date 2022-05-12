import sys

n = int(sys.stdin.readline().replace('\n', ''))

towers = list(map(int, sys.stdin.readline().split(' ')))

stack = [] # 2D list that contains index and length

for i, l in enumerate(towers):
    if len(stack) == 0:
        stack.append([i, l])
        print(0, end=' ')

    else:
        while stack[-1][1] < l:
            stack.pop()

            if len(stack) == 0:
                print(0, end=' ')
                break

        if len(stack) != 0:
            print(stack[-1][0] + 1, end=' ')

    stack.append([i, l])
