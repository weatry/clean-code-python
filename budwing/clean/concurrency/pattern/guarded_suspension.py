"""
Guarded Suspension is a concurrency pattern that is used to manage access to an object or resource that may not be immediately available.
The pattern involves "guarding" a method or operation with a condition that must be satisfied before the operation can proceed.
If the condition is not met, the calling thread is suspended (or "blocked") until the condition becomes true.

This pattern is particularly useful in scenarios where a thread needs to wait for a specific state or condition before it can safely perform an operation.
For example, a thread may need to wait for data to be available before processing it, or it may need to wait for a resource to be released before acquiring it.
The Guarded Suspension pattern typically involves the use of synchronization mechanisms such as locks, condition variables, or semaphores to manage the waiting and notification of threads.
Proper implementation of the Guarded Suspension pattern is essential to avoid issues such as deadlocks, race conditions, and spurious wakeups.
@see <a href="https://en.wikipedia.org/wiki/Guarded_suspension">Guarded suspension - Wikipedia</a>
"""

import threading
import queue
from typing import Any, Optional


class GuardedSuspension:
    def __init__(self):
        self._resource: Any = None
        self._condition = threading.Condition()

    # Method to get the resource, waiting if it's not available
    def get_resource(self) -> Any:
        with self._condition:
            while self._resource is None:
                self._condition.wait()  # Wait until notified that the resource is available
            return self._resource

    # Method to set the resource and notify waiting threads
    def set_resource(self, resource: Any) -> None:
        with self._condition:
            self._resource = resource
            self._condition.notify_all()  # Notify all waiting threads that the resource is now available


class GuardedQueue:
    """
    A simple Guarded Queue implementation using the Guarded Suspension pattern.
    It can be replaced by queue.Queue from python standard library in real applications.
    """
    
    def __init__(self):
        self._queue = []
        self._condition = threading.Condition()

    def get(self) -> Optional[int]:
        with self._condition:
            # use while to avoid spurious wakeup
            while not self._queue:
                try:
                    self._condition.wait()  # Condition not met, wait
                except KeyboardInterrupt:
                    threading.current_thread().interrupt()
                    return None
            return self._queue.pop(0)

    def put(self, value: int) -> None:
        with self._condition:
            self._queue.append(value)
            self._condition.notify_all()  # Condition met, notify waiting threads


def main():
    # Example usage
    guarded_obj = GuardedSuspension()
    
    def consumer():
        print("Waiting for resource...")
        resource = guarded_obj.get_resource()
        print(f"Got resource: {resource}")

    def producer():
        print("Preparing resource...")
        # Simulate some work
        import time
        time.sleep(2)
        guarded_obj.set_resource("Important Data")
        print("Resource set")

    # Start consumer thread
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()
    
    # Start producer thread
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()
    
    consumer_thread.join()
    producer_thread.join()
    
    # Test GuardedQueue
    guarded_queue = GuardedQueue()
    
    def queue_consumer():
        print("Getting element from queue...")
        item = guarded_queue.get()
        print(f"Got queue element: {item}")
        
    def queue_producer():
        print("Putting element to queue...")
        import time
        time.sleep(1)
        guarded_queue.put(42)
        print("Element added to queue")
        
    # Start queue consumer thread
    queue_consumer_thread = threading.Thread(target=queue_consumer)
    queue_consumer_thread.start()
    
    # Start queue producer thread
    queue_producer_thread = threading.Thread(target=queue_producer)
    queue_producer_thread.start()
    
    queue_consumer_thread.join()
    queue_producer_thread.join()


if __name__ == "__main__":
    main()