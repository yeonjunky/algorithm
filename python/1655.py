import sys;from heapq import heappop as p,heappush as u
i,l,t=sys.stdin.readline,len,int
N,m,M=t(i()),[],[]
for _ in range(N):
 n = t(i())
 if not M:u(M, n)
 else:
  if M[0]>n:u(m,-n)
  else:u(M, n)
 a,b=l(M),l(m)
 if a>b+2:u(m,-p(M))
 elif b>=a:u(M,-p(m))
 print(M[0])