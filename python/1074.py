import sys


N, r, c = map(int, sys.stdin.readline().split())
N = 2 ** N
answer = 0

while N > 1:
    half = N // 2
    if 0 <= r < N // 2 and 0 <= c < N // 2:
        c %= half
        r %= half

    elif 0 <= r < N // 2 and N // 2 <= c < N:
        answer += half ** 2
        c %= half
        r %= half

    elif N // 2 <= r < N and 0 <= c < N // 2:
        answer += 2 * half ** 2
        c %= half
        r %= half

    else:
        answer += 3 * half ** 2
        c %= half
        r %= half

    N = half

print(answer)
