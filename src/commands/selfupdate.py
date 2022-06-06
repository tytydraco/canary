import os
import pathlib
import sys

from src.commands.command import Command
from src.commands.gitpull import GitPull
from src.logging.log import Log


class SelfUpdate(Command):
    main_path = pathlib.Path(sys.modules['__main__'].__file__).parent

    def __init__(self):
        super(SelfUpdate, self).__init__(requires_su=False)

    def command(self):
        Log.dbg('Updating our own repo...')
        GitPull.update_repo(self.main_path)
        Log.dbg('Restarting ourselves...')
        os.execv(sys.executable, [sys.executable] + sys.argv)
