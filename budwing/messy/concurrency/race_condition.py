import asyncio
import threading
import time

class Counter:
    """
    Counter class to demonstrate concurrent access to shared data.

    In this class, count is a shared variable which can be accessed by all instances.
    If the class is used in a multithreaded environment, is it thread-safe?
    If the class is used in coroutine environment, is it thread-safe?
    """
    count = 0
    def __init__(self):
        """do we need lock?"""
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
    
    def __init__(self):
        # do some initialization
        pass
    
    @classmethod
    def get_instance(cls):
        """
        Race condition in singleton
        
        Note: This implementation shows what NOT to do. The proper way would
        involve synchronization to prevent race conditions.
        """
        # check and act
        if cls._instance is None:
            # the condition might be changed by other threads 
            # before this thread enters this block
            cls._instance = cls()
        return cls._instance
    
    def withdraw(self, user: User, amount):
        """
        Demonstrates race condition in withdrawal operation.
        
        Check and act pattern that can cause issues in concurrent environment.
        """
        # check and act
        if user.get_balance() >= amount:
            # Simulate some processing time that could allow context switching
            # This makes the race condition more likely to occur
            time.sleep(0.1)

            user.set_balance(user.get_balance() - amount)
            print(f"{threading.current_thread().name} withdraw {amount} successfully, "
                  f"balance: {user.get_balance()}")
        else:
            print(f"{threading.current_thread().name} withdraw failed, insufficient funds. "
                  f"Balance: {user.get_balance()}, Attempt: {amount}")
            
    async def withdraw_async(self, user: User, amount):
        """
        Demonstrates race condition in withdraw operation.
        
        Coroutine is a concurrency model that allows you to write asynchronous code 
        that looks and behaves like synchronous code. It's almost thread-safe, 
        because they are running in an event loop of a single thread.
        But if you run it in an incorrect way, it can lead to race conditions as well.
        """
        
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
    
    print(f"Final balance: {alice.get_balance()}")

    c = Counter()
    print(f"Counter: {c.count}")

if __name__ == "__main__":
    main()