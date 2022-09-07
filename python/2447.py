import sys


def star(n):
    if n == 3:
        return [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]

    else:
        previous = star(n // 3)
        current = []
        
        for i in range(3):
            for j in range(n // 3):
                if i == 1:
                    current.append(previous[j] + [' '] * (n // 3) + previous[j])
                
                else:
                    current.append(previous[j] * 3)
        
        return current

num = int(sys.stdin.readline())

for i in star(num):
    for j in i:
        print(j, end='')
    print("")
