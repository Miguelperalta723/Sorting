# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):

    # loop through n-1 elements
    
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for item in range(cur_index + 1, len(arr)):
            if(arr[item] < arr[smallest_index]):
                smallest_index = item
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]


    return arr





# 1. Start with current index = 0

# 2. For all indices EXCEPT the last index:

#     a. Loop through elements on right-hand-side 
#     of current index and find the smallest element

#     b. Swap the element at current index with the
#     smallest element found in above loop



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    index_length = len(arr) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr



# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.


























# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr