import random


def fill_array(size, low, high):
    result = [0] * size
    i = 0
    while i < size:
        result[i] = random.randint(low, high)
        i += 1
    return result


def bubble_sort(array):
    n = len(array)
    i = 0
    while i < n:
        j = 0
        while j < n - 1 - i:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        i += 1


def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def find_duplicates(sorted_arr, arr):
    seen = {}
    result = []
    i = 0
    while i < len(arr):
        val = arr[i]
        if val not in seen and binary_search(sorted_arr, val):
            result.append(val)
            seen[val] = True
        i += 1
    return result


SIZE = 50

arr1 = fill_array(SIZE, 0, 100)
arr2 = fill_array(SIZE, 0, 100)

bubble_sort(arr1)

print("Sorted array 1:", arr1)
print("array 2:", arr2)
print("-" * 30)
print("Duplicates:", find_duplicates(arr1, arr2))