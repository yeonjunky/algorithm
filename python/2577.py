a = int(input())
b = int(input())
c = int(input())

cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = list(str(a * b * c))

for i in res:
    if i == '0':
        cnt[0] += 1

    elif i == '1':
        cnt[1] += 1

    elif i == '2':
        cnt[2] += 1

    elif i == '3':
        cnt[3] += 1

    elif i == '4':
        cnt[4] += 1

    elif i == '5':
        cnt[5] += 1

    elif i == '6':
        cnt[6] += 1

    elif i == '7':
        cnt[7] += 1

    elif i == '8':
        cnt[8] += 1

    elif i == '9':
        cnt[9] += 1

for i in cnt:
    print(i)