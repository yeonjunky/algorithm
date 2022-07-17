import sys


n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = 100001
left = 0
right = 0
sum = arr[0]

while left < n:
    if sum < s:
        right += 1

        if right == n:
            break

        else:
            sum += arr[right]

    else:
        sum_len = right - left + 1
        result = min(sum_len, result)

        sum -= arr[left]
        left += 1

if result == 100001:
    print(0)
else:
    print(result)
