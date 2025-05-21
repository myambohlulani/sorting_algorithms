# implementation of merge sort using recursion only
# Hlulani Myambo
# 21 May 2025
# time-complexity -> O(n log n)

def merge_sort(array: list[int]) -> list[int]:
    # for only one or less values then the array is sorted
    if len(array) <= 1:
        return array

    # finding the middle value to know where to split from
    middle: int = len(array) // 2

    left_half: list[int] = array[:middle]
    right_half: list[int] = array[middle:]

    sorting_left = merge_sort(left_half)
    sorting_right = merge_sort(right_half)

    return merge(sorting_left, sorting_right)

def merge(left: list[int], right: list[int], result = None, index = 0, index_2 = 0) -> list[int]:
    # initialising a new list
    if result is None:
        result: list = []
    # base case
    if index < len(left) and index_2 < len(right):
        if left[index] < right[index_2]:
            # adding to array
            result.append(left[index])
            # recursive call
            return merge(left, right, result, index + 1, index_2)
        else:
            # adding to array
            result.append(right[index_2])
            # recursive call
            return merge(left, right, result, index, index_2 + 1)

    # merging lists at the end
    result.extend(left[index:])
    result.extend(right[index_2:])

    return result

unsorted_array: list[int] = [3, 7, 6, -10, 15, 23, 5, 55, 12]
sorted_array: list[int] = merge_sort(unsorted_array)

print(sorted_array) #output = [-10, 3, 5, 6, 7, 12, 15, 23, 55]