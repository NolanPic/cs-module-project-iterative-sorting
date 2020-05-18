# time: O(n)
# space: O(1)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
# time: O(log n)
# space: O(1)
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid+1
        if arr[mid] > target:
            right = mid-1

    return -1  # not found
