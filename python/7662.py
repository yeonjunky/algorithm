import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    t = int(input().rstrip())
    min_q = []
    max_q = []
    element_cnt = {}
    q_len = 0

    for _ in range(t):
        operation, n = input().split()
        n = int(n)

        if operation == 'I':
            heapq.heappush(min_q, n)
            heapq.heappush(max_q, -n)
            q_len += 1

            if n not in element_cnt:
                element_cnt[n] = 1
            else:
                element_cnt[n] += 1

        else:
            if q_len > 0:
                if n == 1:
                    while max_q and not element_cnt[-max_q[0]]:
                        heapq.heappop(max_q)
                    if element_cnt[-max_q[0]]:
                        element = -heapq.heappop(max_q)
                        element_cnt[element] -= 1

                else:
                    while min_q and not element_cnt[min_q[0]]:
                        heapq.heappop(min_q)
                    if element_cnt[min_q[0]]:
                        element = heapq.heappop(min_q)
                        element_cnt[element] -= 1
                q_len -= 1

            else:
                max_q.clear()
                min_q.clear()

    while max_q and not element_cnt[-max_q[0]]:
        heapq.heappop(max_q)
    while min_q and not element_cnt[min_q[0]]:
        heapq.heappop(min_q)

    if min_q and max_q:
        print(-heapq.heappop(max_q), heapq.heappop(min_q))
    else:
        print('EMPTY')
