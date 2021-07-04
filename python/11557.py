school = []
alcohol = []

for _ in range(int(input())):
    for _ in range(int(input())):
        a = input().split()
        school.append(a[0])
        alcohol.append(int(a[1]))
    print(school[alcohol.index(max(alcohol))])