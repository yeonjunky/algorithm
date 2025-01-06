m, n = map(int, input().split())
nums = [1 for i in range(n + 1)]
nums[0] = nums[1] = 0

for i in range(2, int(n ** (1 / 2)) + 1):
    if nums[i]:
        for j in range(i * 2, n + 1, i):
            nums[j] = 0

for i, v in enumerate(nums[m:]):
    if v:
        print(i + m)