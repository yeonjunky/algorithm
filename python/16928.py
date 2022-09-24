'''
idea: bfs로 풀이
      사다리, 뱀이 없는 칸은 직전 칸의 주사위 수 + 1
      있는 칸은 사다리, 뱀의 도착 칸에 값 갱신
      어느 칸이 원래 값보다 적은 값으로 도달할 수 있다면,
      값 갱신하고 다시 큐에 넣음
      큐에서 꺼낸 값이 100이면 break, board[100] 출력
'''
import sys
from collections import deque

ls = {}
board = [0] * 101

N, M = map(int, sys.stdin.readline().split())

for _ in range(N + M):
    x, y = map(int, sys.stdin.readline().split())
    ls[x] = y

queue = deque([1])

while queue:
    pos = queue.popleft()

    if pos == 100:
        break

    for i in range(1, 7):
        new_pos = pos + i
        if new_pos <= 100:

            if pos + i in ls:
                if not board[ls[new_pos]] or board[ls[new_pos]] > board[pos] + 1:
                    queue.append(ls[new_pos])
                    board[ls[new_pos]] = board[pos] + 1

            else:
                if not board[new_pos] or board[new_pos] > board[pos] + 1:
                    queue.append(new_pos)
                    board[new_pos] = board[pos] + 1

print(board[100])
