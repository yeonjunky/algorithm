import sys

def is_pelindrome(s: str):
    l = len(s)
    n = l // 2
    for i in range(n):
        if s[i] != s[l - i - 1]:
            return False
    return True

s = sys.stdin.readline().rstrip()

while s != '0':
    if is_pelindrome(s):
        print("yes")
    else:
        print("no")
    s = sys.stdin.readline().rstrip()
