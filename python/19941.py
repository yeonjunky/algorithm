import sys

n, k = map(int, sys.stdin.readline().split(' '))

string = list(sys.stdin.readline().replace('\n', ''))
cnt = 0

for i, c in enumerate(string):
    if c == 'P':
        for j in range(i - k, i + k + 1):
            if j < 0 or j >= n:
                continue

            if string[j] == 'H':
                cnt += 1
                string[j] = ' '
                break

print(cnt)