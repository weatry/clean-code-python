"""
Balking is a concurrency pattern that prevents an object from performing an action 
if it is not in a valid state to do so. The Balking pattern is typically used in 
scenarios where an operation should only be executed when certain conditions are met.
If the conditions are not met, the operation is "balked" or ignored, preventing 
unnecessary processing or potential errors.

This pattern is particularly useful in multi-threaded environments where multiple 
threads may attempt to access or modify the state of an object simultaneously. 
By implementing the Balking pattern, developers can ensure that operations are only 
performed when the object is in a valid state, thus maintaining data integrity and consistency.
"""

import threading
import time


class Document:
    def __init__(self):
        self._is_saved = True
        self._lock = threading.Lock()

    def edit(self):
        with self._lock:
            self._is_saved = False

    def save(self):
        with self._lock:
            if self._is_saved:
                print("Document is already saved. Balking the save operation.")
                return  # Balk if already saved
            
            # Simulate saving process
            print("Saving document...")
            self._is_saved = True


class JobExecutor:
    def __init__(self):
        self._is_running = False
        self._lock = threading.Lock()

    def execute_job(self, job):
        # First check without acquiring the lock for performance
        if self._is_running:
            print(f"{threading.current_thread().name} balked: another job is already running.")
            return  # Balk if a job is already running

        # Acquire lock for thread-safe check and state modification
        with self._lock:
            if self._is_running:
                print(f"{threading.current_thread().name} balked: another job is already running.")
                return  # Double-check within locked block
            
            self._is_running = True

        try:
            job()
        finally:
            with self._lock:
                self._is_running = False  # Reset the state after job completion


def main():
    # Test Document example
    doc = Document()
    doc.edit()
    doc.save()  # Should save the document
    doc.save()  # Should balk

    # Test JobExecutor example
    def job():
        try:
            print("Job started for ", threading.current_thread().name)
            time.sleep(2)  # Simulate long-running job
            print("Job completed for ", threading.current_thread().name)
        except KeyboardInterrupt:
            threading.current_thread().interrupt()

    executor = JobExecutor()
    t1 = threading.Thread(target=executor.execute_job, args=(job,))
    t2 = threading.Thread(target=executor.execute_job, args=(job,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()