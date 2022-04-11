import sys

# catalan number problem

def factorial(n):
    if dp[n]:
        return dp[n]

    else:
        for i in range(1, n + 1):
            dp[i] = i * dp[i - 1]

    return dp[n]

def catalan(n):
    return (factorial(2 * n) // (factorial(n) * factorial(n + 1)))

while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break

    dp = [0] * (2 * n + 1)
    dp[0] = dp[1] = 1

    print(catalan(n))
