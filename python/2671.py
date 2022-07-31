import sys
import re


NOISE = "NOISE"
SUBMARINE = "SUBMARINE"

submarine_string = re.compile('(100+1+|01)+')

string = sys.stdin.readline().rstrip()

if re.fullmatch(submarine_string, string):
    print(SUBMARINE)
else:
    print(NOISE)
