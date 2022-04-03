import sys

n, k = map(int, sys.stdin.readline().split())

previous = [1]
current = [1, 1]

if n == 1:
    print(1)

elif n == 2:
    print(1)

else:
    for i in range(3, n + 1):
        previous = current
        current = [0] * i

        for j in range(len(current)):
            if j == 0 or j == len(current) - 1:
                current[j] = 1
            else:
                current[j] = previous[j - 1] + previous[j]

    print(current[k - 1])