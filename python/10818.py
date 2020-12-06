n = int(input())
li = input().split(' ')
int_list = []

for i in range(0, n):
    int_list.append(int(li[i]))

int_list.sort()
print(int_list[0], int_list[n-1])