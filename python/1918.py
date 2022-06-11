import sys


stack = [] # keeping operators
postfix = []

string = sys.stdin.readline().rstrip()


for i, c in enumerate(string):
    if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        postfix.append(c)

    elif c == '(':
        stack.append(c)

    elif c == ')':
        operator = stack.pop()
        while operator != '(':
            postfix.append(operator)
            operator = stack.pop()

    elif c in ('*', '/'):
        while stack and stack[-1] in ('*', '/'):
            postfix.append(stack.pop())

        stack.append(c)

    elif c in ('+', '-'):
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())

        stack.append(c)

while stack:
    postfix.append(stack.pop())

print("".join(postfix))
