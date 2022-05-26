import signal
import sys

from src.logging.log import Log
from src.net.sockets import Sockets
from src.parser.parser import Parser

sockets = Sockets()


def main():
    sockets.initialize()

    for command in sockets.read():
        Parser.handle_command(command)


def sigint_handler(signum, frame):
    Log.dbg('Closing sockets...')
    sockets.close()
    Log.dbg('Exit!')
    sys.exit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    main()
