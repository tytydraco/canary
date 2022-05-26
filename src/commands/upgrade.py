import os

from src.commands.command import Command


class Upgrade(Command):
    def __init__(self):
        super(Upgrade, self).__init__(requires_su=True)

    def command(self):
        os.system('sudo apt-get update && sudo apt-get -y upgrade')
