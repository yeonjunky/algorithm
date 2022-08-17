import sys


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

dp = [0] * (N + 1)
fixed_seats = []
result = 1

dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

for _ in range(M):
    fixed_seats.append(int(sys.stdin.readline().rstrip()))

if M:
    temp = 0

    for i in range(M):
        result *= dp[fixed_seats[i] - 1 - temp]
        temp = fixed_seats[i]
    result *= dp[N - temp]

else:
    result = dp[N]

print(result)
