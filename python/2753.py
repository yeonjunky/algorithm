year = int(input())

def is_yoon(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 1

    else:
         return 0

print(is_yoon(year))