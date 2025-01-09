a, b = map(int, input().split())

while b != 0:
    re = a % b
    a, b = b, re
print("1" * a, end='')