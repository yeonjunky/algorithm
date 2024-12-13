n,m,*a=map(int,open(0).read().split())
print(sum(m-i in a for i in a)//2)