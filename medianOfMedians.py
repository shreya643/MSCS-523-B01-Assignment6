import random
import time

def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    

    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(group)[len(group)//2] for group in groups]
    
    pivot = median_of_medians(medians, len(medians)//2)
    

    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(low) - len(high)
    
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return median_of_medians(high, k - len(low) - pivot_count)