n,s=open(0)
s=list(map(int,s.split()))
print(sum(s)*100/max(s)/int(n))
#minimal bytes in python
n,*s=map(int,open(0).read().split())
print(sum(s)*100/max(s)/n)