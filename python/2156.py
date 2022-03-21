import sys

n = int(sys.stdin.readline().replace('\n', ''))

wines = []
dp = [0] * n

for i in range(n):
    wines.append(int(sys.stdin.readline().replace('\n', '')))

if n > 2:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(wines[2] + wines[1], max(wines[2] + dp[0], dp[1]))

    for i in range(3, n):
        dp[i] = max(
                    max(wines[i] + dp[i - 2], dp[i - 1]), 
                    max(wines[i] + wines[i - 1] + dp[i - 3], wines[i] + dp[i - 3])
                )

    print(max(dp[-2:]))

else:
    if n == 2:
        print(wines[0] + wines[1])

    elif n == 1:
        print(wines[0])