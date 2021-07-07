# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    for i in range(elements):
        if (len(arrA) == 0):
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif (len(arrB) == 0):
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif (arrA[0] <= arrB[0]):
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right)


# ### Algorithm
# ```
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element 
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
# ```








































# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
