import sys


n = int(sys.stdin.readline().rstrip())

arr = [True] * (n + 1)
arr[0] = arr[1] = False
result = 0
prime_nums = [2]

i = 4 # 짝수 없애기
while i < n:
    arr[i] = 0
    i += 2

i = 3
while i < n + 1:
    if not arr[i]:
        i += 2
        continue

    prime_nums.append(i)

    j = i ** 2

    while j < n + 1:
        arr[j] = False
        j += i * 2

    i += 2

if len(prime_nums) > 1:
    left = 0
    right = 1

    sum = prime_nums[left]

    while right < len(prime_nums):

        if sum < n:
            sum += prime_nums[right]
            right += 1

        else:
            if sum == n:
                result += 1
            sum -= prime_nums[left]
            left += 1

# 1 <= n <= 4000000
# if 문의 조건을 충족 못하는 경우는 n == 1 || n == 2
# n == 1인 경우는 답이 0 n == 2인 경우는 답이 1

if n in prime_nums:
    # n이 소수일 경우, 자기 자신 더하기
    result += 1

print(result)
