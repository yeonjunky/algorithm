import sys


def R(a):
    max_row = 0
    sorted_a = []

    for i in a:
        nums = {}

        for j in i:
            if j != 0:
                if j not in nums:
                    nums[j] = 1
                else:
                    nums[j] += 1

        li = list(nums.items())
        li.sort(key=lambda item: (item[1], item[0]))

        if len(li) > 50:
            li = li[:50]

        max_row = max(len(li) * 2, max_row)

        sorted_row = []

        for k in li:
            sorted_row.extend(k)

        sorted_a.append(sorted_row)

    for i in sorted_a:
        if len(i) < max_row:
            i.extend([0] * (max_row - len(i)))

    return sorted_a, max_row


a = []
time = 0
row = 3
col = 3
result = -1

r, c, k = map(int, sys.stdin.readline().split())

for _ in range(3):
    a.append(list(map(int, sys.stdin.readline().split())))

for _ in range(101):
    if r - 1 < row and c - 1 < col:
        if a[r - 1][c - 1] == k:
            result = time
            break

    # R operation
    if row >= col:
        a, col = R(a)
        time += 1

    # C operation
    else:
        a = [list(sub_a) for sub_a in zip(*a)]
        a, row = R(a)
        a = [list(sub_a) for sub_a in zip(*a)]
        time += 1

print(result)
