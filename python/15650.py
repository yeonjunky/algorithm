'''
idea: 재귀로 오름차순 순열 구하기
'''
import sys

def permutations(current):
    if len(current) < M:
        if current:
            start = current[-1] + 1
        else:
            start = 1

        for i in range(start, N + 1):
            permutations(current + [i])

    else:
        print(*current)
        return

N, M = map(int, sys.stdin.readline().split())

permutations([])
