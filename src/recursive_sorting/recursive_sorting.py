# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    
    merged_arr = []
    
    while len(arrA) >= 1:
        
        # print(f"Array A: {arrA}, Array B: {arrB}, Merged Array: {merged_arr}")
        if arrB == []:
            for j in range(len(arrA)):
                merged_arr.append(arrA.pop(0))
        else:
            if arrA[0] < arrB[0]:
                merged_arr.append(arrA.pop(0))
            else:
                merged_arr.append(arrB.pop(0))
    if arrB != []:
        for k in arrB:
            merged_arr.append(k)
    
    return merged_arr
    # print(merged_arr)
    # print("Hello from merge helper")

# print(merge([1, 4, 5], [0, 3, 7]))



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
        
    arrA = merge_sort(arr[:middle])
    arrB = merge_sort(arr[middle:])


    return merge(arrA, arrB)

    # print("Single Element")
    #     merge(arrA, arrB)
    # return arr


# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
