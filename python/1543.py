import sys

doc = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()

n = len(doc)
word_len = len(word)
i = 0
cnt = 0

while i < n:
    if i > n - word_len:
        break

    if word == doc[i:i + word_len]:
        cnt += 1
        i += word_len
    
    else: 
        i += 1

print(cnt)
