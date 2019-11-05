#TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    
    for i in range(0, len(arr)-1):
        # print(arr)
        current_value = arr[i]
        current_index = i
        smallest_remaining = arr[i+1]
        smallest_remaining_index = i + 1
        #WHY IS THERE NO ARR-1 ??
        for j in range(i+1, len(arr)):
            if smallest_remaining > arr[j]:
                smallest_remaining = arr[j]
                smallest_remaining_index = j
        if current_value > smallest_remaining:
            arr.remove(current_value)
            arr.remove(smallest_remaining)
            arr.insert(current_index, smallest_remaining)
            arr.insert(smallest_remaining_index, current_value)
        # print(f"Current Value: {current_value}, Smallest Remaining: {smallest_remaining}, Smallest Remaining Index: {smallest_remaining_index}")
    return arr
        # 
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
#         # TO-DO: swap




    

# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_count = 1
    while swap_count >= 1:
        swap_count = 0
        for i in range(0, len(arr)-1):
            current_value = arr[i]
            current_index = i
            next_value = arr[i+1]
            next_index = i+1
            # print(arr)
            # print(f"Current Value: {current_value}, Next Value:{next_value}, Swap Count: {swap_count}")
            if current_value > next_value:
                arr.remove(current_value)
                arr.remove(next_value)
                arr.insert(current_index, next_value)
                arr.insert(next_index, current_value)
                swap_count += 1
            
            

    return arr   
    # print(f"\n\nFinal Result: {arr}")
        








        # current = arr[i]
    #     next = arr[i + 1]
    #     if current > next:
    #         current, next = next, current
    # return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr