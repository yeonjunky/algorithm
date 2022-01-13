import random
from sort_algo import bubble_sort

def generate_arr(length):
    arr = []
    while(len(arr) < length):
        num = random.randint(1, 101)
        if num not in arr:
            arr.append(num)

    return arr

def linear_search(arr, val):
    for i in arr:
        if i == val:
            return val

    return None

def I_linear_search(arr, val):
    """
    improved linear search worst case complexity
    """
    is_find = 0

    for i in range(0, int(len(arr)/2)):
        if arr[i] == val:
            print("element found in array at", str(i)+" index")
            is_find = 1
            break

        if arr[len(arr)-(i+1)] == val:
            print("element found in array at", str(len(arr)-(i+1))+" index")
            is_find = 1
            break

    if not is_find:
        print("didn't find value")

def binary_search(arr, val):
    """
    arr: list[int]
    val: int
    binary search works on sorted array
    """
    sorted_arr = bubble_sort(arr) # sort array before search
    left = 0
    right = len(sorted_arr) - 1

    print("sorted array")
    print(sorted_arr)

    while left < right:
        mid = int(left + (right - left) / 2)
        print("mid:", mid, "value:", sorted_arr[mid])

        if sorted_arr[mid] < val:
            left = mid + 1

        elif sorted_arr[mid] > val:
            right = mid - 1

        else:
            print("found value at index {}".format(mid))
            return val

    print("value doesn't exist in array")
    return -1





nums = generate_arr(50)
print(nums)
# print(I_linear_search(arr, 5))
binary_search(nums, 56)