n, l = input().split()
n = int(n)
label = 0

for i in range(n):
    label += 1
    while l in str(label):
        label += 1

print(label)
