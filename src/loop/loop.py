import threading
import time


class Loop:
    thread: threading.Thread
    __running = True

    def __init__(self):
        self.thread = threading.Thread(target=self.loop)

    def loop(self):
        while self.__running:
            # TODO: run loops
            time.sleep(1)

    def start_loop(self):
        self.thread.start()

    def stop_loop(self):
        self.__running = False
