import logging
import concurrent.futures
import threading
import time

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
    	''' Ten update powoduje bledne dzialanie - zjawisko wyscigu
    	'''
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)

    def locked_update(self, name):
    	''' Ten update uzywa lock-a i nie ma problemu z wyscigiem
    	'''
        logging.info("Thread %s: starting update", name)
        

        with self._lock:
			local_copy = self.value
			local_copy += 1
			time.sleep(0.1)
			self.value = local_copy
			logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info("Testing update. Ending value is %d.", database.value)