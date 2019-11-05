# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    
    merged_arr = []
    
    while len(arrA) >= 1:
        pointerA = arrA[0]
        pointerB = arrB[0]
        print(f"Array A: {arrA}, Array B: {arrB}, Merged Array: {merged_arr}")
        if arrB == []:
            for j in arrA:
                merged_arr.append(j)
        elif pointerA < pointerB:
            merged_arr.append(pointerA)
            arrA.remove(pointerA)
        else:
            merged_arr.append(pointerB)
            arrB.remove(pointerB)
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
    first = 0
    last = len(arr) - 1
    middle = (last-first) // 2
        
    arrA = arr[:middle]
    arrB = arr[middle:]

    print(f"Full Array: {arr}")
    print(f"First: {first}, Last: {last}, Middle: {middle}")
    print(f"Left Hand Side: {arrA}, Right Hand Side: {arrB}")


    while len(arr) > 1:
        # merge_sort(arrB)
        merge_sort(arrA)
    
    
    
    if len(arr) <= 1:
        return arr[0]

    print("All down to one")

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
