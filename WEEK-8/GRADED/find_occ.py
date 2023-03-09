def first(arr, x, n):
    low = 0
    high = n - 1
    res = None
     
    while (low <= high):
         
        mid = (low + high) // 2
         
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
             
        # If arr[mid] is same as x, we
        # update res and move to the left
        # half.
        else:
            res = mid
            high = mid - 1
 
    return res
 
def last(arr, x, n):
     
    low = 0
    high = n - 1
    res = None
     
    while(low <= high):
         
        # Normal Binary Search Logic
        mid = (low + high) // 2
         
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
             
        # If arr[mid] is same as x, we
        # update res and move to the Right
        # half.
        else:
            res = mid
            low = mid + 1
 
    return res
    
def findOccOf(L, x):
    try:
        return (L.index(x), len(L)-1-L[::-1].index(x))
    except Exception:
        return (None, None)
