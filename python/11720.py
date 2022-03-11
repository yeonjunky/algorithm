import sys

n = input()

nums = sys.stdin.readline().replace('\n', '')
result = 0

for i in nums:
    result = result + int(i)

print(result)