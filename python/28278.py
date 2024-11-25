import sys

n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(n):
    command = sys.stdin.readline().rstrip().split()
    if (command[0] == '1'):
        stack.append(int(command[1]))

    elif (command[0] == '2'):
        res = -1 if len(stack) == 0 else stack.pop()
        print(res)

    elif (command[0] == '3'):
        print(len(stack))

    elif (command[0] == '4'):
        print(int(not(len(stack))))

    elif (command[0] == '5'):
        res = -1 if len(stack) == 0 else stack[-1]
        print(res)