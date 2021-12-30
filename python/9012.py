import sys

def is_valid(paren):
    stack = []
    for i in paren:
        if i == '(':
            stack.append(1)
        
        elif i == ')' and stack != []:
            stack.pop()

        elif i == ')' and stack == []:
            return False

    if stack:
        return False
        
    return True


n = int(sys.stdin.readline())

for _ in range(n):
    paren = sys.stdin.readline()
    if is_valid(paren):
        print("YES")
    else:
        print("NO")