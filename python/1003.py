import sys

T = int(sys.stdin.readline().rstrip())

dp = [0] * 41 # N <= 40
dp[0] = (1, 0)
dp[1] = (0, 1)
last_idx = 2

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())

    if dp[N]:
        print(dp[N][0], dp[N][1])

    else:
        for i in range(last_idx, N + 1):
            zeros = dp[i - 1][0] + dp[i - 2][0]
            ones = dp[i - 1][1] + dp[i - 2][1]
            dp[i] = (zeros, ones)

            last_idx = i

        print(dp[N][0], dp[N][1])
