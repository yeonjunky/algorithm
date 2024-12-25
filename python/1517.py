def merge(li, start, end):
    global cnt

    m = (start + end) // 2
    left = start
    right = m + 1
    last_sort_idx = start

    for i in range(start, end + 1):
        tmp[i] = a[i]
    while left <= m and right <= end:
        if tmp[left] > tmp[right]:
            a[last_sort_idx] = tmp[right]
            cnt += right - last_sort_idx
            last_sort_idx += 1
            right += 1
        else:
            a[last_sort_idx] = tmp[left]
            last_sort_idx += 1
            left += 1
    while left <= m:
        a[last_sort_idx] = tmp[left]
        last_sort_idx += 1
        left += 1

    while right <= end:
        a[last_sort_idx] = tmp[right]
        last_sort_idx += 1
        right += 1


def mergesort(li, start, end):
    if start < end:
        m = (start + end) // 2
        mergesort(li, start, m)
        mergesort(li, m + 1, end)
        merge(li, start, end)

n, a = open(0)
n = int(n)
a = list(map(int, a.split()))
cnt = 0
tmp = [0] * (n)
mergesort(a, 0, n - 1)
print(cnt)