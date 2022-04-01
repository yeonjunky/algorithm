import sys

string = sys.stdin.readline().rstrip()
arr = string.split('-')
result = 0

for i, li in enumerate(arr):
    if '+' in li:
        arr[i] = sum(list(map(int, arr[i].split('+'))))

result = int(arr[0])

for i in range(1, len(arr)):
    result -= int(arr[i])

print(result)