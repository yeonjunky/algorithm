import random
import sort_algo

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
        print("didnt find value")

def binary_search(arr, val):
    """
    binary search works only sorted array
    """
    arr = sort_algo.bubble_sort(arr)
    half_index = len(arr)

    
    




arr = generate_arr(50)
print(arr)
# print(I_linear_search(arr, 5))
I_linear_search(arr, 5)
