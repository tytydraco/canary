import pathlib
import signal
import sys

from src.init.init import Init
from src.logging.log import Log
from src.net.sockets import Sockets
from src.parser.parser import Parser

sockets = Sockets()


def main():
    Log.setup_logfiles()
    Init.run_init_scripts()
    sockets.initialize()

    for conn, command in sockets.read():
        valid = Parser.handle_command(command)

        try:
            if valid:
                conn.send(b'>\n')
            else:
                conn.send(b'!\n')
        except BrokenPipeError:
            pass


def sigint_handler(signum, frame):
    Log.dbg('Closing sockets...')
    sockets.close()
    Log.dbg('Exit!')
    sys.exit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    main()
