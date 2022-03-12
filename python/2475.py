import sys

nums = sys.stdin.readline().split(' ')
total = 0

for i in nums:
    total = total + int(i) ** 2
    # print(int(i) ** 2, total)

print(total % 10)
