import sys

line = sys.stdin.readline().rstrip()
cnt = 0
while line:
    if (line == "gum gum for jay jay"):
        cnt += 1
    line = sys.stdin.readline().rstrip()

print(cnt)
