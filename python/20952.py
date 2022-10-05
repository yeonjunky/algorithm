import sys


N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
remainder = [0] * 7
cnt = 0

for i in range(N):
    if not remainder[A[i] % 7]:
        remainder[A[i] % 7] += 1
        cnt += 1
    if cnt == 7:
        break

b_sum = 0
check = 0
for i in range(M):
    temp = 7 - (check + B[i]) % 7 if (check + B[i]) % 7 != 0 else 0

    if remainder[temp]:
        if cnt == 1:
            continue
        remainder[temp] = 0
        cnt -= 1

    check = (check + B[i]) % 7
    b_sum += B[i]
    b_sum %= 1000000007

result = [(A[i] + b_sum) % 1000000007 for i in range(N) if remainder[A[i] % 7]]
print(len(result))
print(*result)
