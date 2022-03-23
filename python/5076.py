import sys

while True:
    html = sys.stdin.readline().replace('\n', '')
    if html == '#':
        break
    stack = []
    is_legal = True

    opening = False
    closing = False

    tag_name = ""
    space = 0

    for i, c in enumerate(html):
        if opening:
            if c == ' ':
                space = i

            elif c == '>':
                opening = False
                is_tag = False

                if html[i - 1] != '/':
                    if space:
                        stack.append(tag_name[:space-1])
                        space = 0
                    else: 
                        stack.append(tag_name)

                tag_name = ""

            else:
                tag_name += c

        if closing:
            if c == '>':
                closing = False

                if stack:
                    last_opening = stack.pop()

                else:
                    is_legal = False
                    break

                if tag_name.replace('/', '') != last_opening:
                    is_legal = False
                    break

                tag_name = ''

            else:
                tag_name += c


        if c == '<':
            if html[i + 1] == '/':
                closing = True
            else:
                opening = True

    if stack or not is_legal:
        print("illegal")
    else:
        print("legal")
        