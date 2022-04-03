import sys

bracket = {
    ']': '[',
    ')': '('
}

while True:
    stack = []
    is_balanced = True
    string = sys.stdin.readline().rstrip()

    if string == '.':
        break

    for i in string:
        if i in ['(', '[']:
            stack.append(i)

        elif i in [')', ']']:
            if stack:
                v = stack.pop()
                if bracket[i] != v:
                    is_balanced = False
                    break
            else:
                is_balanced = False
                break


    if is_balanced and not stack:
        print('yes')
    else:
        print('no')