'''
idea: 연속된 0과 1의 개수를 세고 적은 수를 출력
      둘 중 적은 수로 뒤집는게 최소
'''

import sys


num = sys.stdin.readline().rstrip()
zeros = 0
ones = 0
previous = ''

for i in num:
    if previous != i:
        if i == '0':
            zeros += 1
        else:
            ones += 1

    previous = i

print(min(zeros, ones))
