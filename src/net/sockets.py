import socket

from src.logging.log import Log
from src.other.config import LISTEN_PORT


class Sockets:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def initialize(self):
        Log.dbg('Binding...')
        self.__try_bind()
        Log.dbg('Preparing listener...')
        self.__listen()
        Log.dbg('Waiting for connections...')
        self.__accept_loop()

    def __try_bind(self):
        try:
            self.soc.bind(('', LISTEN_PORT))
        except socket.error as message:
            Log.err(f'Bind failed: {message[0]}: {message[1]}')

    def __listen(self):
        self.soc.listen()

    def __accept_loop(self):
        while True:
            conn, addr = self.soc.accept()
            Log.dbg(f'Connected to: {addr[0]}:{addr[1]}')
