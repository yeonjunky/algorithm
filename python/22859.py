import sys
import re
h = sys.stdin.readline().rstrip()[6:-7]
h = h.replace('<div ', '\n')
h = h.replace('</div>', '')
h = h.replace('<p>', '\n')
h = h.replace('</p>', '')
h = re.sub(r'</?[A-Za-z]+ *>', '', h)
h = h.replace('>', '')
h = h.replace('=', ' : ')
h = h.replace('"', '')
h = re.sub(' +', ' ', h)
print(h[1:])
