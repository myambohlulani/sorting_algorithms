# implementation of selection sort using recursion
# Myambo Hlulani
# 2 june 2025
# time-complexity -> O(n^2)

def selection_sort(array: list[int]):
    for outer in range(len(array)):
        minimum = outer
        for inner in range(1 + outer, len(array)):
            if array[minimum] > array[inner]:
                minimum = inner
        array[minimum], array[outer] = array[outer], array[minimum]

    return array

array = [64, 34, 25, 5, 22, 11, 90, 12]
print(selection_sort(array))