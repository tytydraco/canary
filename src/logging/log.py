import inspect
import os.path
import sys
from datetime import date, datetime

from src.other.config import DEBUG, LOG_FILE_DIR_PATH, LOGGING

_PFX_DBG = ' * '
_PFX_ERR = ' ! '


class Log:
    @staticmethod
    def __log(msg):
        if LOGGING:
            today = date.today()
            datestamp = today.strftime("%m-%d-%y")
            filename = f'canary_{datestamp}.txt'
            filepath = f'{LOG_FILE_DIR_PATH}/{filename}'
            with open(filepath, 'a') as f:
                f.write(msg)
                f.write('\n')
        print(msg)

    @staticmethod
    def setup_logfiles():
        if not os.path.exists(LOG_FILE_DIR_PATH):
            os.mkdir(LOG_FILE_DIR_PATH)

    @staticmethod
    def dbg(msg):
        if DEBUG:
            caller = inspect.stack()[1].function
            timestamp = datetime.now()
            Log.__log(f'[{timestamp}] [{caller}] \033[92m{_PFX_DBG}{msg}\033[0m')

    @staticmethod
    def err(msg, bail=True):
        if DEBUG:
            caller = inspect.stack()[1].function
            timestamp = datetime.now()
            Log.__log(f'[{timestamp}] [{caller}] \033[91m{_PFX_ERR}{msg}\033[0m')
        else:
            Log.__log(f'\033[91m{_PFX_ERR}{msg}\033[0m')

        if bail:
            sys.exit(1)
