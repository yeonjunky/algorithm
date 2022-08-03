import sys

N = int(sys.stdin.readline().rstrip())

solution = list(map(int, sys.stdin.readline().split()))

left = 0
right = len(solution) - 1
minimum = 600000000000
index = (left, right)

while left < right:
    value = solution[left] + solution[right]

    if abs(value) < minimum:
        minimum = abs(value)
        index = (left, right)

    if value > 0:
        right -= 1

    elif value < 0:
        left += 1

    else:
        index = (left, right)
        break

print(solution[index[0]], solution[index[1]])
