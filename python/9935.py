import sys

string = sys.stdin.readline().strip()
bomb = list(sys.stdin.readline().strip())
stack = []

i = 0
bomb_len = len(bomb)

for i, c in enumerate(string):
    stack.append(c)

    if len(stack) < bomb_len:
        continue

    else:
        if stack[-bomb_len:] == bomb:
            del stack[-bomb_len:]

print("".join(stack) if stack else "FRULA")
