import threading
import time

from src.loop.process_check import ProcessCheck
from src.other.config import LOOP_DELAY, LOOPS


class Loop:
    loops = [
        ProcessCheck
    ]

    thread: threading.Thread
    __running = True

    def __init__(self):
        self.thread = threading.Thread(target=self.loop)

    def loop(self):
        while self.__running:
            for loop_command in self.loops:
                loop_command().execute()
            time.sleep(LOOP_DELAY)

    def start_loop(self):
        if LOOPS:
            self.thread.start()

    def stop_loop(self):
        if LOOPS:
            self.__running = False
