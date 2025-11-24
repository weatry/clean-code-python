import threading
import queue
import time
import random
import logging

logger = logging.getLogger(__name__)

# create a queue with a max size of 5
q = queue.Queue(maxsize=5)

def producer(name, n):
    for i in range(n):
        item = f"{name}-item-{i}"
        logger.info(f"Producer {name} producing {item}")
        q.put(item)  # blocks until space available
        time.sleep(random.uniform(0.1, 0.5))
    logger.info(f"Producer {name} finished.")

def consumer(name):
    while True:
        try:
            # wait at most 2 seconds for an item, it's used to quit gracefully
            # q.get will raise Empty if no item available after 2 seconds
            item = q.get(timeout=2)
            logger.info(f"Consumer {name} consuming {item}")
            time.sleep(random.uniform(0.2, 0.6))
            q.task_done()  # tells queue that task is done
        except queue.Empty:
            logger.error(f"Consumer {name} timed out, exiting.")
            break

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s %(filename)s %(levelname)s:%(message)s"
    )

    prod_thread = threading.Thread(target=producer, args=("P1", 10))
    cons_thread1 = threading.Thread(target=consumer, args=("C1",))
    cons_thread2 = threading.Thread(target=consumer, args=("C2",))

    prod_thread.start()
    cons_thread1.start()
    cons_thread2.start()

    prod_thread.join()
    q.join()  # waits for all items to be consumed

    print("All done!")