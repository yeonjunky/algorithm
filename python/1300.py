n = int(input())
k = int(input())
start = 1
# 중복되는 수들이 있어 b[k] < k
end = k

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, n + 1):
        # 각 행에서 mid보다 작은 숫자의 개수. 
        # mid // i == j
        cnt += min(mid // i, n)
    if cnt < k:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)