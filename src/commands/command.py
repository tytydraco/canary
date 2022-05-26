import ctypes
import os
from abc import ABC, abstractmethod

from src.logging.log import Log


class Command(ABC):
    requires_su = False

    def __init__(self, requires_su=requires_su):
        self.requires_su = requires_su

    def __check_su(self):
        if self.requires_su:
            Log.dbg('Checking privileges')
            try:
                is_admin = os.getuid() == 0
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if not is_admin:
                Log.err('Command requires elevated privileges', bail=False)
                return False
        return True

    def execute(self):
        if not self.__check_su():
            return
        Log.dbg('Executing command')
        self.command()

    @abstractmethod
    def command(self):
        pass
