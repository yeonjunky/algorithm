n, *a = open(0)
n = int(n)
a = [(int(a[i]), i) for i in range(n)]
sorted_a = sorted(a)
cnt = [0] * n

for i in range(n - 1):
    cnt[i] = sorted_a[i][1] - a[i][1]

print(max(cnt) + 1)