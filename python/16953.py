import sys

"""
A에서 B로
연산: 왼쪽에 1 붙이기, 곱하기 2

B에서 A로 가기
연산: 나누기 10, 나누기 2
2를 곱했을 때 1은 나올 수 없으므로 맨 오른쪽 자리가 1이라면 나누기 10
그 외에는 나누기 2
"""

a, b = map(int, sys.stdin.readline().split())
cnt = 1

while b > a:
    if b % 10 == 1:
        b //= 10

    else:
        b /= 2

    cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)
