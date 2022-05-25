import inspect
import sys

from src.other.config import DEBUG

_PFX_DBG = ' * '
_PFX_ERR = ' ! '


class Log:
    @staticmethod
    def dbg(msg):
        if DEBUG:
            caller = inspect.stack()[1].function
            print(f'[{caller}] \033[92m{_PFX_DBG}{msg}\033[0m')

    @staticmethod
    def err(msg, bail=True):
        if DEBUG:
            caller = inspect.stack()[1].function
            print(f'[{caller}] \033[91m{_PFX_ERR}{msg}\033[0m')
        else:
            print(f'\033[91m{_PFX_ERR}{msg}\033[0m')

        if bail:
            sys.exit(1)
