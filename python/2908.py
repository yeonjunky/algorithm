import sys

a, b = map(int, sys.stdin.readline().replace('\n', '')[::-1].split(' '))

higher_num = a if a > b else b

print(higher_num)