import sys


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

if c[0] == 1:
    k = c[1] - 1
    num = list(range(1, n + 1))

else:
    pass