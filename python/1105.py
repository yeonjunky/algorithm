import sys

l, r = sys.stdin.readline().split()
cnt = 0

if len(l) == len(r):
    sub = int(r) - int(l)
    print(len(l) - sub)

    if sub:
        for i in range(len(l) - len(str(sub))):
            if l[i] == '8' and r[i] == '8':
                cnt += 1
    else:
        for i in range(len(l)):
            if l[i] == '8':
                cnt += 1

    print(cnt)  

else:
    print(0)