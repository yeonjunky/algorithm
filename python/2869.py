a, b, v = map(int, input().split())

x = (v-a)/(a-b)+1

if x%1 != 0:
    print(int(x+1))
else:
    print(int(x))

