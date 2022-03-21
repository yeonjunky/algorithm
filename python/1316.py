import sys

t = int(sys.stdin.readline().replace('\n', ''))
cnt = 0

for i in range(t):
    chars = []
    current = ''
    isgroup = True

    string = sys.stdin.readline().replace('\n', '')

    for j in string:
        if current != j:
            current = j
            if current in chars:
                isgroup = False
                break
            chars.append(current)

    if isgroup:
        cnt += 1

print(cnt)
