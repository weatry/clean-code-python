import asyncio
import threading
import time

class User:
    """
    A simple class to represent a user with a balance.
    """
    name: str
    balance: float
    _lock: threading.Lock

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self._lock = threading.Lock()

def transfer(source: User, target: User, amount: float):
    with source._lock:
        print(f"{threading.current_thread().name}: got {source.name}'s lock")
        time.sleep(0.1)
        with target._lock:
            print(f"{threading.current_thread().name}: got {target.name}'s lock")
            print(f"{threading.current_thread().name}: transferring {amount} from {source.name} to {target.name}")

def deadlock_example():
    alice = User("Alice", 100)
    bob = User("Bob", 100)
    threads = [
        threading.Thread(target=transfer, args=(alice, bob, 20), name="Thread A"),
        threading.Thread(target=transfer, args=(bob, alice, 30), name="Thread B"),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

async def save(user: User):
    """
    This is a deadlock-like example in coroutine which uses lock in a wrong way.
    It's not a real deadlock, it actually blocks the event loop and the whole program.
    """
    print(f"{user.name}: trying to acquire lock")
    with user._lock:  # it's a threading lock, won't yield control even when it's locked
        print(f"{user.name}: got lock, saving...")
        await asyncio.sleep(1)  # yield control to other tasks, but not the lock
        print(f"{user.name}: releasing lock")

async def deadlock_like_example():
    # start two coroutine
    alice = User("Alice")
    await asyncio.gather(save(alice), save(alice))

if __name__ == "__main__":
    # deadlock_example()
    asyncio.run(deadlock_like_example())
