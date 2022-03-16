import sys

string = sys.stdin.readline().replace('\n', '')

num = 0
stack = 0
is_laser = False

for i, p in enumerate(string):
    if p == '(':
        if string[i + 1] == ')':
            num += stack
            is_laser = True

        else:
            stack += 1
    else:
        if is_laser:
            is_laser = False
        else:
            stack -= 1
            num += 1

print(num)