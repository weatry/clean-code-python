"""
Active Object is a concurrency pattern that decouples method execution from
method invocation to enhance concurrency and simplify synchronized access to
an object.
The Active Object pattern introduces an intermediary/proxy that manages
method requests, allowing clients to invoke methods asynchronously without
blocking.
This intermediary/proxy typically consists of a queue to hold method requests
and a dedicated thread to process these requests sequentially.
By using the Active Object pattern, multiple clients can interact with the
active object concurrently, while the internal state of the object remains
consistent and thread-safe.
This pattern is particularly useful in scenarios where method calls may
involve long-running operations or when the object needs to maintain a
consistent state across multiple threads.

@see <a href="https://en.wikipedia.org/wiki/Active_object_pattern">Active
     object pattern - Wikipedia</a>

The main components of the Active Object pattern include:
1. Proxy: The interface that clients interact with to invoke methods
asynchronously.
2. Activation Queue: A queue that holds method requests until they can
be processed.
3. Scheduler: A component that manages the execution of method requests
from the activation queue.
4. Servant: The actual object that performs the requested operations.
5. Method Request: An object that encapsulates a method call, including
its parameters and the logic to execute it.
6. Worker Thread: A dedicated thread that processes method requests from
the activation queue.
"""

import threading
import queue
from abc import ABC, abstractmethod
from concurrent.futures import Future


class BusinessOperation(ABC):
    @abstractmethod
    def business_operation1(self) -> Future:
        pass

    @abstractmethod
    def business_operation2(self) -> Future:
        pass


class Servant:
    """
    Servant is the component that actually performs the operations requested by
    clients in the Active Object pattern.
    """
    def __init__(self):
        self.data = 0

    def business_operation1(self) -> int:
        print("Servant is executing businessOperation1")
        self.data += 1
        return self.data  # some non-blocking operation

    def business_operation2(self) -> int:
        print("Servant is executing businessOperation2")
        self.data -= 1
        return self.data  # some non-blocking operation


class MethodRequest(ABC):
    """
    MethodRequest is an abstract class representing a request to be executed by
    the Servant.
    It encapsulates the details of the request and provides an interface for
    execution.
    It's actually a command in Command Pattern.
    """
    @abstractmethod
    def execute(self, servant: Servant) -> None:
        pass


class BusinessOperation1(MethodRequest):
    """
    Concrete MethodRequest to perform the business operation.
    """
    def __init__(self, future: Future):
        self.future = future

    def execute(self, servant: Servant) -> None:
        result = servant.business_operation1()
        self.future.set_result(result)


class BusinessOperation2(MethodRequest):
    """
    Concrete MethodRequest to perform the business operation.
    """
    def __init__(self, future: Future):
        self.future = future

    def execute(self, servant: Servant) -> None:
        result = servant.business_operation2()
        self.future.set_result(result)


class ActiveObject(BusinessOperation):
    def __init__(self):
        self.queue = queue.Queue()  # Activation Queue
        self.servant = Servant()    # Servant instance
        self.running = True
        self.worker = threading.Thread(target=self._run)
        self.worker.start()

    def _run(self) -> None:
        while self.running:
            try:
                request = self.queue.get(timeout=1)
                request.execute(self.servant)
                self.queue.task_done()
            except queue.Empty:
                continue  # Check if still running

    def business_operation1(self) -> Future:
        future = Future()
        request = BusinessOperation1(future)
        self.queue.put(request)
        return future

    def business_operation2(self) -> Future:
        future = Future()
        request = BusinessOperation2(future)
        self.queue.put(request)
        return future

    def shutdown(self) -> None:
        self.running = False
        self.worker.join()

    @staticmethod
    def main():
        active_object = ActiveObject()
        result1 = active_object.business_operation1()
        result2 = active_object.business_operation2()

        try:
            print("Result of businessOperation1:", result1.result())
            print("Result of businessOperation2:", result2.result())
        except Exception as e:
            print(e)

        active_object.shutdown()


if __name__ == "__main__":
    ActiveObject.main()