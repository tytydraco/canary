import signal
import sys

from src.init.init import Init
from src.logging.log import Log
from src.loop.loop import Loop
from src.net.sockets import Sockets
from src.parser.parser import Parser

sockets = Sockets()
loop = Loop()


def main():
    Log.setup_logfiles()
    Init.run_init_scripts()
    sockets.initialize()
    loop.start_loop()

    for conn, command in sockets.read():
        valid = Parser.handle_command(command)

        try:
            if valid:
                conn.send(b'>\n')
            else:
                conn.send(b'!\n')
        except BrokenPipeError:
            pass

    cleanup()


def cleanup():
    Log.dbg('Closing sockets...')
    sockets.close()
    Log.dbg('Exit!')
    loop.stop_loop()
    sys.exit()


# noinspection PyUnusedLocal
def sigint_handler(signum, frame):
    cleanup()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    main()
