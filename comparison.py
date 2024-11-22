import random
import time
from medianOfMedians import median_of_medians
from quicksort import quickselect

def performance_comparison():
    input_sizes = [ 500, 1000, 5000, 10000]
    print(f"{'Size':<10} {'Median of Medians (s)':<25} {'Quickselect (s)':<20}")
    print("=" * 60)
    
    for size in input_sizes:
        arr = [random.randint(1, 100000) for _ in range(size)]
        k = size // 2  # Median index
        
        # Median of Medians
        start = time.time()
        median_of_medians(arr, k)
        median_time = time.time() - start
        
        # Quickselect
        start = time.time()
        quickselect(arr, k)
        quickselect_time = time.time() - start
        
        # Print the results
        print(f"{size:<10} {median_time:<25.6f} {quickselect_time:<20.6f}")

# Run the comparison
performance_comparison()