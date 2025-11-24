from multiprocessing import Process, Queue
from queue import Empty
import logging

logger = logging.getLogger(__name__)

"""
Producer-Consumer Problem

Producer-Consumer Problem is a classic synchronization problem in operating systems. 
The problem is to synchronize two processes such that the producer process produces the data and consumer process consumes the data. 

In this program, we use a queue to synchronize the producer and consumer processes.
"""
# global q can not be shared between processes
# q = Queue() 

def producer(q: Queue):
    """
    Producer process
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(filename)s %(levelname)s: %(message)s"
    )
    logger.info("Starting producer process")

    items = ["item1", "item2", "item3"]
    for item in items:
        logger.info("Producing %s", item)
        q.put(item)

def consumer(q: Queue):
    """
    Consumer process
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(filename)s %(levelname)s: %(message)s"
    )
    logger.info("Starting consumer process")

    while True:
        try:
            item = q.get(timeout=1)
            logger.info("Consuming %s", item)
        except Empty:
            logger.info("Queue is empty within 1 second")
            break

if __name__ == "__main__":
    
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()