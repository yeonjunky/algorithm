n = int(input())
scores = map(int, input().split())

arr = list(scores)
arr.sort()
m = arr[n-1]

modified_arr = list(map(lambda x: x / m * 100, arr))
average = sum(modified_arr) / n
print(average)