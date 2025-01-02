import sys

n = int(sys.stdin.readline())
pos = []
neg = []
result = []
is_zero = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        is_zero = 1

pos.sort(reverse=1)
neg.sort()

if len(pos) % 2 == 1:
    result.append(pos.pop())

if len(neg) % 2 == 1:
    if is_zero:
        neg.pop()
    else:
        result.append(neg.pop())

while pos:
    a, b = pos.pop(), pos.pop()
    if a * b == a or a * b == b:
        result.append(a), result.append(b)
    else:
        result.append(a * b)

while neg:
    a, b = neg.pop(), neg.pop()
    result.append(a * b)

print(sum(result))