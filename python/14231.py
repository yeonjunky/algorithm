import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
b = a[0]
dp = [1 for _ in range(n)]
for i in range(1, n):
	for j in range(i):
		if a[i] > a[j] and dp[i] < dp[j] + 1:
			dp[i] = dp[j] + 1
print(max(dp))