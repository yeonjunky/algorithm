import sys
from math import ceil

t = int(sys.stdin.readline())
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())

    if h >= n:
        print(n * 100 + 1)
    else:
        if n % h != 0:
            print(n % h * 100 + ceil(n / h))

        else:
            print(h * 100 + ceil(n / h))