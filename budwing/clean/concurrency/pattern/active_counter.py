"""
Active Counter is a simplified implementation of the Active Object
concurrency pattern that provides asynchronous methods
to increment and retrieve the value of a counter. The Active Counter
decouples method invocation from method execution
by using a dedicated worker thread and a queue to hold tasks.

Clients can invoke the increment() and get_value() methods, which return
Future objects representing the results of
these operations. The actual execution of these operations is handled by the
worker thread, ensuring thread-safe
access to the counter's internal state.

This pattern is particularly useful in scenarios where multiple threads need
to interact with a shared resource
without blocking each other, allowing for improved concurrency and
responsiveness.

@see <a href="https://en.wikipedia.org/wiki/Active_object_pattern">Active
     object pattern - Wikipedia</a>
"""

import threading
import queue
from abc import ABC, abstractmethod
from concurrent.futures import Future


class Counter(ABC):
    @abstractmethod
    def increment(self) -> Future:
        pass

    @abstractmethod
    def get_value(self) -> Future:
        pass


class ActiveCounter(Counter):
    def __init__(self, initial_value: int):
        self.queue = queue.Queue()
        self.value = initial_value
        self.running = True
        self.worker = threading.Thread(target=self._run)
        self.worker.start()

    def _run(self) -> None:
        try:
            while self.running:
                try:
                    task = self.queue.get(timeout=1)
                    task()
                    self.queue.task_done()
                except queue.Empty:
                    continue  # Check if still running
        except Exception as e:
            print(f"Worker thread exception: {e}")

    # Asynchronous method to increase the counter
    def increment(self) -> Future:
        future = Future()
        def task():
            try:
                self.value += 1
                # time.sleep(0.1)  # Simulate time-consuming operation
                future.set_result(self.value)
            except Exception as e:
                future.set_exception(e)
        self.queue.put(task)
        return future

    # Asynchronous method to get the current counter value
    def get_value(self) -> Future:
        future = Future()
        def task():
            try:
                # time.sleep(0.05)  # Simulate time-consuming operation
                future.set_result(self.value)
            except Exception as e:
                future.set_exception(e)
        self.queue.put(task)
        return future

    def shutdown(self) -> None:
        self.running = False
        self.worker.join()

def main():
    counter = ActiveCounter(0)

    print("Starting Active Object example...")
    from concurrent.futures import ThreadPoolExecutor
    
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = []
        for i in range(5):
            future = pool.submit(lambda: counter.increment())
            futures.append(future)

        for future in futures:
            try:
                result = future.result()
                print(f"Result: {result}")  # output the incremented value
            except Exception as e:
                print(e)

    counter.shutdown()


if __name__ == "__main__":
    main()