n = int(input())
l = list(map(int, input().split()))
cnt = 0
l.sort()

for i in range(n):
    start = 0
    end = n - 1
    while start < end:
        if l[start] + l[end] == l[i]:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif l[start] + l[end] < l[i]:
            start += 1
        else:
            end -= 1

print(cnt)