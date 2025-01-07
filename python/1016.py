m, n = map(int, input().split())
is_prime = [1] * (n - m + 1)

i = 2
while i ** 2 <= n:
    mul = m // i ** 2
    while mul * (i ** 2) <= n:
        if 0 <= mul * (i ** 2) - m <= n - m:
            is_prime[mul * (i ** 2) - m] = 0
        mul += 1
    i += 1

print(sum(is_prime))