def sum_of_digits(num):
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num = int(num / 10)
    return sum_digits 

def find_self_num():
    num = 1
    not_self_num = 0
    li = [i for i in range(1, 10001)]
    while(num <= 10000):
        not_self_num = num + sum_of_digits(num)
        num += 1
        try:
            li.remove(not_self_num)
        except:
            pass

    for i in li:
        print(i)


find_self_num()
