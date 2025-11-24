import asyncio
import random
import threading
import time

import logging

logger = logging.getLogger(__name__)

class User:
    """
    A simple class to represent a user with a balance.
    """
    name: str
    balance: float
    _lock: threading.Lock
    _async_lock: asyncio.Lock

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self._lock = threading.Lock()
        self._async_lock = asyncio.Lock()

def transfer_try_lock(source: User, target: User, amount: float):
    """
    By using acquire(blocking=False) with a backoff strategy, we can avoid deadlock.
    """
    while True:
        if source._lock.acquire(blocking=False):
            try:
                logger.info(f"{threading.current_thread().name}: got {source.name}'s lock")
                time.sleep(0.1)
                if target._lock.acquire(blocking=False):
                    try:
                        logger.info(f"{threading.current_thread().name}: got {target.name}'s lock")
                        time.sleep(0.1)
                        logger.info(f"{threading.current_thread().name}: transferred {amount} from {source.name} to {target.name}")
                        break
                    finally:
                        target._lock.release()
                else:
                    logger.info(f"{threading.current_thread().name}: failed to get {target.name}'s lock")
            finally:
                source._lock.release()
                logger.info(f"{threading.current_thread().name}: released {source.name}'s lock")
        else:
            logger.info(f"{threading.current_thread().name}: failed to get {source.name}'s lock")
        
        time.sleep(random.uniform(0.001, 1))

def transfer_lock_timeout(source: User, target: User, amount: float):
    """
    By using acquire(timeout=x), we can avoid deadlock.
    """
    while True:
        if source._lock.acquire(timeout=0.1):
            try:
                logger.info(f"{threading.current_thread().name}: got {source.name}'s lock")
                time.sleep(0.1)
                if target._lock.acquire(timeout=0.1):
                    try:
                        logger.info(f"{threading.current_thread().name}: got {target.name}'s lock")
                        time.sleep(0.1)
                        logger.info(f"{threading.current_thread().name}: transferred {amount} from {source.name} to {target.name}")
                        break
                    finally:
                        target._lock.release()
                else:
                    logger.info(f"{threading.current_thread().name}: failed to get {target.name}'s lock")
            finally:
                source._lock.release()
                logger.info(f"{threading.current_thread().name}: released {source.name}'s lock")
        else:
            logger.info(f"{threading.current_thread().name}: failed to get {source.name}'s lock")
        
        time.sleep(random.uniform(0.001, 1))

def transfer_fix_order(source: User, target: User, amount: float):
    """
    By using acquire(timeout=x), we can avoid deadlock.
    """
    if source.name > target.name:  # fix the order of locks
        source, target = target, source
    with source._lock:
        logger.info(f"{threading.current_thread().name}: got {source.name}'s lock")
        time.sleep(0.1)
        with target._lock:
            logger.info(f"{threading.current_thread().name}: got {target.name}'s lock")
            time.sleep(0.1)
            logger.info(f"{threading.current_thread().name}: transferred {amount} from {source.name} to {target.name}")
       
def deadlock_example():
    alice = User("Alice", 100)
    bob = User("Bob", 100)
    t = transfer_fix_order
    threads = [
        threading.Thread(target=t, args=(alice, bob, 20), name="Thread A"),
        threading.Thread(target=t, args=(bob, alice, 30), name="Thread B"),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

async def save(user: User):
    """
    Never use threading lock in asyncio coroutine
    """
    logger.info(f"{user.name}: trying to acquire lock")
    async with user._async_lock:  # it's a asyncio lock, will yield control to other tasks
        logger.info(f"{user.name}: got lock, saving...")
        await asyncio.sleep(1)  # yield control to other tasks, but not the lock
        logger.info(f"{user.name}: releasing lock")

async def deadlock_like_example():
    # start two coroutine
    alice = User("Alice")
    await asyncio.gather(save(alice), save(alice))

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s %(filename)s %(levelname)s:%(message)s"
    )
    # deadlock_example()
    asyncio.run(deadlock_like_example())
