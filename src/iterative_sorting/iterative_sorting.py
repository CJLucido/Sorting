# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements

    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
    i = 0   
    for i in range(0, len(arr)-1): #doesn't include the very last one because it should already be sorted to proper position, would break if tried?

    #a. Loop through elements on right-hand-side 
    #of current index and find the smallest element
            #assume current number is smallest, 
           
            j = i+1
            while j in range(i+1, +\
                len(arr)): #DOES include the very last one because we need to check it's value against everything that comes before it, not including it here would make it so that we didn't compare 8 to 7 and it would think it was done with 8,9, (invisible) 7
                smallest = arr[i]

                if smallest <= arr[j]: #smallest less than the next_number
                    j +=1 
                else:
                    #order matters
                    smallest = arr[j]
                    arr[j] = arr[i]  
                    arr[i] = smallest
                     
                    
    #b. Swap the element at current index with the
    #smallest element found in above loop
  


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