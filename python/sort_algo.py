arr = [4, 3, 2, 8, 5, 6, 0, 9, 1, 7]

def swap(arr, right, left):
    temp = arr[right]
    arr[right] = arr[left]
    arr[left] = temp
    return arr

def selection_sort(arr):
    for i in range(0, len(arr)):
        minindex = i
        for j in range(i+1, len(arr)): # j -> minindex
            if(arr[minindex] > arr[j]):
                minindex = j
        arr = swap(arr, i, minindex)
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - (i+1)): # (len - 1) - i 
            if(arr[j] > arr[j+1]):
                arr = swap(arr, j, j+1)
    return arr

def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while(j>=0 and arr[j] > key):
            arr = swap(arr, j, j+1)
            j -= 1
    return arr

def merge_sort(arr):
    mid = int(len(arr) / 2)
    

def quick_sort(arr, start, end):
    
    if start < end:
        p = quick_partition(arr, start, end)

        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)


def quick_partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]
    print("-------------------")
    print("start:", start, "end:", end, "pivot:", pivot)

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
        print("start:", start, "end:", end)
        print(arr)

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    print(arr)

    return end


# print(quick_sort(arr, 0, len(arr)-1))
quick_sort(arr, 0, len(arr)-1)