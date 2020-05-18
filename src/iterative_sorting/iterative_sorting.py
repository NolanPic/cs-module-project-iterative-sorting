# time: O(n^2)
# space: O(1)
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # loop thru the rest of the list, starting
        # to the right of cur_index, to find the next smallest
        for j in range(cur_index+1, len(arr)):
            # Find the next smallest index.
            # If arr[i] is less than the item
            # at the current smallest index,
            # set the smallest index to i
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # Next, now that we have the smallest index,
        # we need to swap the item at the current
        # index with this item.
        # Swap the values:
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

# time: O(n^2)
# space: O(1)
def bubble_sort(arr):
    # no sorting necessary if there is one or less items
    if len(arr) <= 1:
        return arr
    # loop thru arr
    # for each item, compare that item to the next;
    # if the next item is smaller, swap the items.
    # Keep track of whether a swap was performed.
    # If there was, another iteration is necessary--
    # if there wasn't, the sort is finished.
    for i in range(len(arr) -1):
        # set a var for storing whether a
        # swap was performed on this iteration
        swap_performed = False
        for j in range(len(arr) -1):
            if arr[j] > arr[j+1]:
                # if the current element is larger
                # than the next, swap them
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_performed = True
        # if no swap was performed on this teration,
        # break out of the loop and thus end the sort
        if not swap_performed:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
