heights = []

for i in range(0, 9):
    heights.append(int(input()))

for i in range(0,9):

    sum = 0
    copied_height = heights

    for j in range(0, 9):

        for h in range(0, 9):

            if i == j:
                pass

            else:
                sum += heights[j]

            if sum == 100:
                break