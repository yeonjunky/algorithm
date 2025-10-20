import sys
s = set(int(i) for i in sys.stdin)
print(*(i for i in range(1, 31) if i not in s), sep='\n')