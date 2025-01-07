n = int(input())
is_prime = [True] * (1003002)
is_prime[0] = is_prime[1] = 0
result = 0

for i in range(2, int(1003001 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, 1003001 + 1, i):
            is_prime[j] = False


for i in range(n, 1003001):
    if is_prime[i]:
        str_num = str(i)
        start = 0
        end = len(str_num) - 1
        while start <= end:
            if str_num[start] != str_num[end]:
                break
            start += 1
            end -= 1
        if start > end:
            print(i)
            break