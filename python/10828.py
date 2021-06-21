import sys

n = int(sys.stdin.readline().split()[0])
stack = []

for _ in range(n):
    command = sys.stdin.readline().replace("\n", "")

    if command[:4] == "push":
        stack.append(int(command.split(" ")[-1]))
    
    elif command == "pop":
        if len(stack) != 0:
            print(stack[-1])
            stack.__delitem__(-1)
        else:
            print('-1')
    
    elif command == "size":
        print(len(stack))

    elif command == "empty":
        l = len(stack)
        if l > 0:
            print('0')
        else:
            print('1')

    else:
        l = len(stack)
        if l > 0:
            print(stack[-1])
        else:
            print('-1')
