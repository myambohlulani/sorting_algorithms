# implementation of quick sort
# 02 June 2025
# Hlulani Myambo

def quick_sort(array, left, right):
    if right > left:
        pivot_index = partition(array, left, right)
        quick_sort(array, left, pivot_index - 1)
        quick_sort(array, pivot_index + 1, right)

def partition(array, low, high):
    pivot = array[high]
    i = low

    for j in range(low, high):
        if pivot >= array[j]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]

    return i

array = [64, 34, 25, 5, 22, 11, 90, 12]
quick_sort(array, 0, len(array) - 1)
print(array)