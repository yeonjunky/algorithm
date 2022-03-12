import sys

def sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        arr1 = arr[:mid]
        arr2 = arr[mid:]

        sort(arr1)
        sort(arr2)

        i = 0
        j = 0
        k = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
            k += 1

        while i < len(arr1):
            arr[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            arr[k] = arr2[j]
            j += 1
            k += 1



num_len = int(sys.stdin.readline().replace('\n', ''))
nums = list(map(int, sys.stdin.readline().split(' ')))

sort(nums)

print(nums[0] * nums[num_len - 1])
