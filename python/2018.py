n = int(input())
i, j = 1, 2
s = 3
cnt = 1

while i < (n // 2 + 1):
    if s < n:
        j += 1
        s += j
    else:
        if s == n:
            cnt += 1
        s -= i
        i += 1

print(cnt)