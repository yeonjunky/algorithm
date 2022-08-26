"""
idea: 최소인 두 수의 곱은 최소
      모든 순간에 얻을 수 있는 최소를 얻고
      result에 result * 1000000007(문제 조건: 100000007 의 나머지 출력)을 곱해주면 
      해당 TC에서의 최소를 얻음
"""

import sys
import heapq

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())

    pq = list(map(int, sys.stdin.readline().split()))

    if N == 1:
        print(1)

    else:
        heapq.heapify(pq)
        pq_len = N
        result = 1

        while pq_len > 1:
            compose_energy = heapq.heappop(pq) * heapq.heappop(pq)
            result = result * compose_energy % 1000000007
            heapq.heappush(pq, compose_energy)
            pq_len -= 1

        print(result)
