arr = []
for i in range(0, 9):
    arr.append(int(input()))
    if(i == 0):
        max_num = arr[0]
        index = 0
    else:
        if(max_num > arr[i]):
            pass
        else:
            max_num = arr[i]
            index = i

print(str(max_num) + ' \n' + str(index + 1))