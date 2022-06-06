import socket
import time

from src.logging.log import Log
from src.other.config import LISTEN_PORT, SOCKET_BUF_SIZE, SOCKET_BIND_RETRY_DELAY


class Sockets:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def initialize(self):
        Log.dbg('Binding...')
        self.__try_bind()
        Log.dbg('Preparing listener...')
        self.__listen()

    def __try_bind(self):
        while True:
            if self.__try_bind_once():
                break
            time.sleep(SOCKET_BIND_RETRY_DELAY)
        Log.dbg('Bound!')

    def __try_bind_once(self):
        try:
            self.soc.bind(('', LISTEN_PORT))
            return True
        except socket.error as message:
            Log.err(f'Bind failed: {message}', bail=False)
            return False

    def __listen(self):
        self.soc.listen()

    def close(self):
        self.soc.close()

    def read(self):
        while True:
            conn, addr = self.soc.accept()
            Log.dbg(f'Connected to: {addr[0]}:{addr[1]}')

            try:
                conn.send(b'<')
                Log.dbg('Listening for input...')
                _data = conn.recv(SOCKET_BUF_SIZE)
                if not _data:
                    continue
                data = _data.decode().strip()
                if data == '':
                    conn.send(b'x')
                    continue
                Log.dbg(f'Read: {data}')
                conn.send(b'...')
                yield conn, data
            except Exception:
                Log.err('Connection interrupted', bail=False)
                continue
            finally:
                conn.close()
                Log.dbg(f'Closed connection to: {addr[0]}:{addr[1]}')
