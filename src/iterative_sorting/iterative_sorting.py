# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    i = 0
    while i in range(0, len(arr) - 1): #arr[i+1] and 

        # if i > (len(arr) - 1):
        #     return
        arr = arr
        if arr[i] > arr[i+1]:
            smaller = arr[i+1]
            larger = arr[i]

            arr[i] = smaller
            arr[i+1] = larger
            i = 0

        elif arr[i] < arr[i+1]:

            i += 1



    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr