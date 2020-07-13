# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    indx_a = 0
    indx_b = 0

    for i in range(elements):
        if indx_a == len(arrA):
            merged_arr[i] = arrB[indx_b]
            indx_b += 1
        elif indx_b == len(arrB):
            merged_arr[i] = arrA[indx_a]
            indx_a += 1
        elif arrA[indx_a] < arrB[indx_b]:
            merged_arr[i] = arrA[indx_a]
            indx_a += 1
        else:
            merged_arr[i] = arrB[indx_b]
            indx_b += 1


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = merge_sort(arr[0:mid])
    right_arr = merge_sort(arr[mid:len(arr)])

    arr = merge(left_arr, right_arr)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

