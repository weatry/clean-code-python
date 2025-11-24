import threading
import logging

logger = logging.getLogger(__name__)

class DoubleCheckedLocking:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """
        Double checked locking pattern can avoid the overhead of
        locking when the instance has been created.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = object.__new__(cls)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s %(filename)s %(levelname)s:%(message)s"
    )
    s1 = DoubleCheckedLocking()
    s2 = DoubleCheckedLocking()

    logger.info("s1 is s2: %s",s1 is s2)