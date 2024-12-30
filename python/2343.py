import sys


n, m = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))

start = max(v)
end = sum(v)

while (start <= end):
    mid = (start + end) // 2
    bluray_t = 0
    cnt = 1

    for t in v:
        if bluray_t + t > mid:
            cnt += 1
            bluray_t = 0
        bluray_t += t
    
    if cnt <= m:
        end = mid - 1
    else: 
        start = mid + 1

print(start)