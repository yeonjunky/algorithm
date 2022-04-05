import re
import sys

t = int(sys.stdin.readline().rstrip())
reg = re.compile('(100+1+|01)+')

for _ in range(t):
    string = sys.stdin.readline().rstrip()
    res = reg.fullmatch(string)

    if res:
        print("YES")
    else:
        print("NO")
