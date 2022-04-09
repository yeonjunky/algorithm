import sys

n = int(sys.stdin.readline().replace('\n', ''))
memo = [0] * (n + 1)

for i in range(1, n + 1):
    memo[i] = i

    for j in range(0, i):
        if j * j > i:
            break

        if j * j == i:
            memo[i] = 1
            break

        if memo[i] > memo[i - j * j] + 1:
            memo[i] = memo[i - j * j] + 1

print(memo[n])