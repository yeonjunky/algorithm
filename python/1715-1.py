import heapq

n, *card = open(0)
n = int(n)
card = list(map(int, card))
compare_cnt = 0

heapq.heapify(card)

while len(card) > 1:
    a, b = heapq.heappop(card), heapq.heappop(card)
    compare_cnt += a + b
    heapq.heappush(card, a + b)

print(compare_cnt)