'''
누적합을 % m 한 값으로 업데이트
0인 원소를 카운트 해서 cnt에 더함
(0 ~ i 까지의 누적합 % m == 0 이라서)
(A + b) % m == ((a % m) + (b % m)) % m
값이 같은 원소 두 개를 선택해 (I, j) (누적합[j] % m - 누적합[I] % m) % m == 0 이므로,
I - 1 ~ j 까지의 누적합 % m 또한 0
-> 모든 원소에 대해 nC2 한 값을 cnt에 더함.
'''

from itertools import accumulate

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * m

ssum = list(accumulate(a))

for i, v in enumerate(ssum):
    ssum[i] = v % m
    c[v % m] += 1

cnt = ssum.count(0)
for i in c:
    cnt += i * (i - 1) // 2
print(cnt)