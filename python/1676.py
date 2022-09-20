import sys


N = int(sys.stdin.readline().rstrip())
sum = 0

sum += N // 5
sum += N // 25
sum += N // 125

print(sum)
