"""
idea: 입력은 양수, 음수 + 0 으로 분리하여 리스트에 저장하기

      양수는 내림차순으로 정렬, 제일 큰 수와 그 다음 큰 수 합 혹은 곱이 최대
      두 수중 하나라도 1이 포함된다면 합이 최대
      그렇지 않다면 곱이 최대

      음수는 오름차순으로 정렬, 가장 작은 수 * 그 다음 작은 수 만 최대
      0 이 있다면 제일 큰 수 * 0 으로 없애기

      위처럼 모든 상황에서 최대인 수를 얻고 sum에 더해주면 그 합이 최대.
"""

import sys


N = int(sys.stdin.readline().rstrip())
positive = []
negative = []
sum = 0

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())

    if num > 0:
        positive.append(num)

    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

for i in range(0, len(positive), 2):
    if i + 1 < len(positive):
        sum += max(positive[i] + positive[i + 1], positive[i] * positive[i + 1])
    else:
        sum += positive[i]

for i in range(0, len(negative), 2):
    if i + 1 < len(negative):
        sum += negative[i] * negative[i + 1]
    else:
        sum += negative[i]

print(sum)
