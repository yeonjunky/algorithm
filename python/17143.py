import sys

s = sys.stdin.readline().replace('\n', '')
tag = False
stack = ""
result = ""

for i in s:
    if i == '<':
        result += stack[::-1]
        stack = ""
        tag = True
        result += i

    elif i == '>':
        tag = False
        result += i

    elif not tag and i == " ":
        result += stack[::-1]
        stack = ""
        result += i

    elif tag and i == " ":
        result += i

    elif tag:
        result += i

    else:
        stack += i

if len(s) > len(result):
    result += stack[::-1]

print(result)
