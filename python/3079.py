import sys


n, m = map(int, sys.stdin.readline().split())

times = []

for _ in range(n):
    times.append(int(sys.stdin.readline().rstrip()))

left = 0
right = max(times) * m
result = 987654321987654321

while left <= right:
    mid = (left + right) // 2

    # 입국심사를 통과한 사람들 수
    cnt = sum(mid // t for t in times)

    if cnt >= m:
        # 통과한 사람의 수가 m보다 많으면 result 갱신
        result = mid
        right = mid - 1

    else:
        # 통과한 사람의 수가 m보다 적으면 더 큰수를 찾기
        left = mid + 1

print(result)
