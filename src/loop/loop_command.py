from abc import ABC, abstractmethod

from src.logging.log import Log


class LoopCommand(ABC):
    def execute(self):
        Log.dbg('Executing loop command')
        self.command()

    @abstractmethod
    def command(self):
        pass
