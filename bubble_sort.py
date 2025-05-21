# implementation of bubble sort using recursion
# Myambo Hlulani
# 20 May 2025
# time-complexity -> O(n^2)

def bubble_sort(array: list[int], length = None,  index = 0, swapped: bool = False):
    # computing lenght freshly
    if length is None:
        length = len(array)

    # it is sorted if only 1 item is left
    if length <= 1:
        return

    if index >= length - 1:
        if not swapped:
            return
        return bubble_sort(array, length - 1, 0, False)

    # swapping
    if array[index] > array[index + 1]:
        array[index], array[index + 1] = array[index + 1], array[index]
        swapped = True

    return bubble_sort(array, length, index + 1, swapped)

test_case: list[int] = [2, 1, 10, 4, 3, 11, 6, 5, 7, -10]
bubble_sort(test_case)
print(test_case) #output = [-10, 1, 2, 3, 4, 5, 6, 7, 10, 11]