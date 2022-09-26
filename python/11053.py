import sys


N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
dp = [1] * len(nums)
previous = nums[0]

for i in range(len(nums)):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
