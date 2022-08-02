import sys
from itertools import combinations


chickens = []
closest_home = [] # closest homes from chicken
homes = []

N, M = map(int, sys.stdin.readline().split())

for i in range(1, N + 1):
    s = sys.stdin.readline().split()
    for j, v in enumerate(s):
        if v == '1':
            homes.append((i, j + 1))

        elif v == '2':
            chickens.append((i, j + 1))

if M == 1:
    distance = [0] * len(chickens)

    for i, c in enumerate(chickens):
        for h in homes:
            distance[i] += abs(c[0] - h[0]) + abs(c[1] - h[1]) # sum of distances from chicken to homes

    result = min(distance)
    
else:
    combination = list(combinations(chickens, M))
    distance = [0] * len(combination)

    for i, com in enumerate(combination):
        for h in homes:
            temp = 100000000000

            for c in com:
                temp = min(temp, abs(c[0] - h[0]) + abs(c[1] - h[1]))

            distance[i] += temp

    result = min(distance)

print(result)
