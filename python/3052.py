a = []
check = []


for i in range(0, 10):
    num = int(input(""))
    a.append(num % 42)
    if num % 42 not in check:
        check.append(num % 42)

print(len(check))