'''
idea: 모든 문자열에 대해 문자열이 AB일 때, A는 10, B는 1 만큼 더해줌
      위 작업에서 제일 큰 수가 나온 알파벳부터 순서대로 9 ~ 0을 순서대로
      곱해 sum에 더해준다면 최대값 완성
'''
import sys

n = int(sys.stdin.readline().rstrip())
strs = []
current_num = 9
sum = 0
char_cnt = {}
longest_len = 0

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    longest_len = max(longest_len, len(s))

    strs.append(s)

idx = longest_len

while idx > 0:
    for s in strs:
        if idx <= len(s):
            char = s[-1 * idx]

            if char not in char_cnt:
                char_cnt[char] = 10 ** (idx - 1)

            else:
                char_cnt[char] += 10 ** (idx - 1)

    idx -= 1

sorted_keys = list(char_cnt.keys())
sorted_keys.sort(key=lambda char: char_cnt[char], reverse=True)

for c in sorted_keys:
    sum += char_cnt[c] * current_num
    current_num -= 1

print(sum)
