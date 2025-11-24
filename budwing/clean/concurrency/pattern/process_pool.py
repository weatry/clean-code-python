from concurrent.futures import ProcessPoolExecutor
import math
import time

# CPU bound task：calculate square root of a big number
# the function must be able to be serialized by pickle
def cpu_bound_task(n):
    return math.sqrt(n ** 2 + n)

if __name__ == "__main__":  # must have this line when using multiprocessing
    """if the upper line is missing, the program will be in a dead loop on Windows"""

    numbers = range(1000000, 1000010)
    
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_bound_task, numbers))
    end = time.time()
    
    print(f"results: {results[:3]}...") 
    print(f"time consumed: {end - start:.2f} seconds")