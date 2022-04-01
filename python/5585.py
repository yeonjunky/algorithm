a = [500,100,50,10,5,1];m=1000-int(input().rstrip());c=0
for i in a:c+=m//i;m%=i
print(c)