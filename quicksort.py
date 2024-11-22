import random
import time

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    

    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(low) - len(high)
    
    if k < len(low):
        return quickselect(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return quickselect(high, k - len(low) - pivot_count)
