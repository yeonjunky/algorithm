import sys


def shuffle(cards, k):
    if k == 0:
        return cards[::-1]
    return shuffle(cards[-1 * 2**k:], k - 1) + cards[:-1 * 2**k]

N = int(sys.stdin.readline().rstrip())
k_arr = [(i, j) for i in range(1, (N + 1) // 2) for j in range(1, (N + 1) // 2)]

initial_cards = [i for i in range(1, N + 1)]
cards = list(map(int, sys.stdin.readline().split()))

for k in k_arr:
    shuffled = shuffle(shuffle(initial_cards, k[0]), k[1])

    if shuffled == cards:
        print(*k)
        break
