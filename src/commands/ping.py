import os

from src.commands.command import Command


class Ping(Command):
    def __init__(self):
        super(Ping, self).__init__(requires_su=False)

    def command(self):
        return
