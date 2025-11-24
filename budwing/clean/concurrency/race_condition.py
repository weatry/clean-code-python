import asyncio
import threading
import time

import logging

logger = logging.getLogger(__name__)

class Counter:
    """
    Counter class to demonstrate concurrent access to shared data.

    In multithreading environment, multiple threads can access the same shared data 
    at the same time. If two or more threads access the shared data at the same time, 
    it may lead to race condition, where the output is dependent on the sequence 
    or timing of uncontrollable events.

    On the contrary, in coroutines, the concurrency model is almost thread-safe, 
    because they are running in an event loop of a single thread. Since there is 
    only one thread, there is no need to use locks to protect the shared data.
    """
    count = 0
    def __init__(self):
        """
        There's no await, so the execution will be executed without interruptions.
        """
        Counter.count += 1

        # BTW, it's not correct to use self.count, 
        # because self.count is a instance variable.
        # self.count += 1

class User:
    """
    Simple user class to mimic the Java User class.
    """
    def __init__(self, username, balance=0.0):
        self.username = username
        self._balance = balance
        # lock for thread
        self._lock = threading.Lock()
        # lock for coroutine
        self._async_lock = asyncio.Lock()
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, balance):
        self._balance = balance


class RaceCondition:
    """
    Example of race condition.
    
    Race Condition is a behavior where the output is dependent on the sequence 
    or timing of uncontrollable events such as thread scheduling.
    It becomes a problem when two or more threads access shared data and try 
    to change it at the same time.
    If the access to the shared data is not properly synchronized, it can lead 
    to inconsistent or incorrect results.
    """
    _instance = None
    _lock = threading.Lock()
    
    def __init__(self):
        # do some initialization
        pass
    
    @classmethod
    def get_instance(cls):
        """
        By using a class level lock, we can ensure that only one instance 
        of the class is created.
        But it may cause performance issues, because even if the instance
        is already created, it still needs the lock to be acquired.
        """
        with cls._lock:
            # check and act
            if cls._instance is None:
                # the condition might be changed by other threads 
                # before this thread enters this block
                cls._instance = cls()

        return cls._instance
    
    @classmethod
    def get_instance_dcl(cls):
        """
        Double-checked locking pattern can prevent the lock acquisition 
        if the instance has already been created.
        """
        if cls._instance is None:
            # the condition might be changed by other threads 
            # before this thread enters this block
            with cls._lock:
                # check and act
                if cls._instance is None:
                    cls._instance = cls()

        return cls._instance
    
    def withdraw(self, user: User, amount):
        """
        Demonstrates race condition in withdrawal operation.
        
        Check and act pattern that can cause issues in concurrent environment.
        """
        with user._lock:
            # check and act
            if user.get_balance() >= amount:
                # Simulate some processing time that could allow context switching
                # This makes the race condition more likely to occur
                time.sleep(0.1)
                
                user.set_balance(user.get_balance() - amount)
                logger.info(f"{threading.current_thread().name} withdraw {amount} successfully, "
                    f"balance: {user.get_balance()}")
            else:
                logger.info(f"{threading.current_thread().name} withdraw failed, insufficient funds. "
                    f"Balance: {user.get_balance()}, Attempt: {amount}")
            
    async def withdraw_async(self, user: User, amount):
        """
        For coroutines, we can use asyncio.Lock() to prevent race condition.
        asyncio.Lock() is a coroutine-safe lock, but it's not thread-safe, 
        because coroutines are running in an event loop of a single thread.
        Other threads can still access the shared data at the same time.
        """
        
        async with user._async_lock:
            # check and act
            if user.get_balance() >= amount:
                # Simulate some processing time that could allow context switching
                # This makes the race condition more likely to occur
                await asyncio.sleep(0.1) # for example, database update
                user.set_balance(user.get_balance() - amount)


def main():
    """
    Main function to show multithreading and race condition.
    """
    r = RaceCondition.get_instance()
    alice = User("Alice", 100.0)
    threads = []
    for i in range(5):
        t = threading.Thread(
            target=r.withdraw, 
            args=(alice, 30.0),
            name=f"Thread-{i+1}"
        )
        threads.append(t)
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
    
    logger.info(f"Final balance: {alice.get_balance()}")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s %(filename)s %(levelname)s:%(message)s"
    )
    main()