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
        # Get the smallest and current values:
        smallest_val = arr[smallest_index]
        current_val = arr[cur_index]
        # Swap the values:
        arr[cur_index] = smallest_val
        arr[smallest_index] = current_val
        

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
