from src.commands.command import Command


class GitPull(Command):
    def __init__(self):
        super(GitPull, self).__init__(requires_su=False)

    def command(self):
        return
