import threading
import time
import multiprocessing

times = 100_000_000
# CPU-bound task
def cpu_bound_task(n):
    while n > 0:
        n -= 1

def multi_threading():
    # single thread
    start = time.perf_counter()
    cpu_bound_task(times)
    single_thread_time = time.perf_counter() - start

    # multi threads(each thread run half of the task)
    start = time.perf_counter()
    t1 = threading.Thread(target=cpu_bound_task, args=(times/2,))
    t2 = threading.Thread(target=cpu_bound_task, args=(times/2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    multi_thread_time = time.perf_counter() - start

    print(f"single thread: {single_thread_time:.2f} seconds")
    print(f"two threads: {multi_thread_time:.2f} seconds")

def multi_processing():
    # single process
    start = time.perf_counter()
    cpu_bound_task(times)
    single_process_time = time.perf_counter() - start

    # multi processes(each process run half of the task)
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=cpu_bound_task, args=(times/2,))
    p2 = multiprocessing.Process(target=cpu_bound_task, args=(times/2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    multi_process_time = time.perf_counter() - start
    print(f"single process: {single_process_time:.2f} seconds")
    print(f"two processes: {multi_process_time:.2f} seconds")

if __name__ == "__main__":
    # multi_threading()
    multi_processing()
