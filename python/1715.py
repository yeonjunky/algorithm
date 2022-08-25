import sys
import heapq

"""
idea: 우선순위 큐에서 두 차례 가장 작은 수를 pop
      두 수의 합을 sum에 더해주기.
      
      두 수의 합에서 최소인 수를 얻고싶다.
      -> 가장 작은 두 수를 더한다.
      위 두 줄을 반복하여 입력으로 얻은 묶음을 줄여나간다면 
      그 결과가 곧 최소 비교 횟수이다.
"""

N = int(sys.stdin.readline().rstrip())
pq = []

for _ in range(N):
    heapq.heappush(pq, int(sys.stdin.readline().rstrip()))

arr_len = len(pq)
sum = 0

while arr_len > 1:
    num_combined = heapq.heappop(pq) + heapq.heappop(pq)
    sum += num_combined
    heapq.heappush(pq, num_combined)
    arr_len -= 1

print(sum)
