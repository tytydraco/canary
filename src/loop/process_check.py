from src.logging.log import Log
from src.loop.loop_command import LoopCommand


class ProcessCheck(LoopCommand):
    def command(self):
        Log.dbg('Checking essential processes...')
