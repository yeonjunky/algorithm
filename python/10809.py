import sys

pos = [-1] * 26
string = sys.stdin.readline().replace('\n', '')

for i, c in enumerate(string):
    index = ord(c) - 97

    if pos[index] == -1:
        pos[index] = i

for i in pos:
    print(i, end=' ')