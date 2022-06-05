import os

from src.commands.command import Command
from src.logging.log import Log


class GitPull(Command):
    __LOCAL_REPOS = [
        '/home/pi/testrepo',
    ]

    def __init__(self):
        super(GitPull, self).__init__(requires_su=False)

    @staticmethod
    def update_repo(repo_path):
        if not os.path.exists(repo_path):
            Log.err(f'Repo does not exist: {repo_path}', bail=False)
        else:
            os.system(f'git -C {repo_path} pull')

    def command(self):
        for repo_path in self.__LOCAL_REPOS:
            GitPull.update_repo(repo_path)
