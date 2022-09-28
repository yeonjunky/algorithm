import sys
i=sys.stdin.readline
N,x=int(i()),[]
for _ in range(N):x.append(int(i()))
s,m,p=sum(x),max(x),print
if 2*m-s>=0:p(2*m-s)
else:p(s%2)