import os

from src.commands.command import Command


class Reboot(Command):
    def __init__(self):
        super(Reboot, self).__init__(requires_su=True)

    def command(self):
        os.system('reboot')
