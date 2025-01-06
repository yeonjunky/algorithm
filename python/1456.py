a, b = map(int, input().split())
is_prime = [True] * (int(b ** 0.5) + 1)
is_prime[1] = False
cnt = 0

for i in range(2, int(b ** 0.5) + 1):
    if is_prime[i]:
        if i ** 2 > int(b ** 0.5):
            break
        for j in range(i * 2, int(b ** 0.5) + 1, i):
            is_prime[j] = False

for i in range(2, len(is_prime)):
    if is_prime[i]:
        res = i ** 2
        while res < a:
            res *= i
        while a <= res <= b:
            cnt += 1
            res *= i

print(cnt)