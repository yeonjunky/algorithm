n = int(input())
arr = [0] * (2001)

for _ in range(n):
    arr[int(input()) + 1000] = 1

for i in range(2001):
    if arr[i]: 
        print(i - 1000)

# 숏코딩
print(*sorted(map(int,[*open(0)][1:])))