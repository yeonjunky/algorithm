import sys
sys.setrecursionlimit(10000)

def is_prime(num):
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True

def dfs(num, l):
    if l == n:
        sys.stdout.write(str(num) + '\n')
        return 
    for i in [1, 3, 7, 9]:
        if i % 2 == 0:
            continue
        if is_prime(10 * num + i):
            dfs(10 * num + i, l + 1)


n = int(input())
for i in [2, 3, 5, 7]:
    dfs(i, 1)