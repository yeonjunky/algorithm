import itertools as i
s,f=open(0),lambda:map(int,s.readline().split())
n,m=f()
arr=list(f())
sum=[0, *i.accumulate(arr)]
for _ in range(m):
 i,j=f()
 print(sum[j]-sum[i-1])