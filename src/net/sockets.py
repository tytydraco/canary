import socket

from src.logging.log import Log
from src.other.config import LISTEN_PORT, SOCKET_BUF_SIZE


class Sockets:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def initialize(self):
        Log.dbg('Binding...')
        self.__try_bind()
        Log.dbg('Preparing listener...')
        self.__listen()

    def __try_bind(self):
        try:
            self.soc.bind(('', LISTEN_PORT))
            return True
        except socket.error as message:
            Log.err(f'Bind failed: {message}')
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
                conn.send(b'+\n')

                while True:
                    Log.dbg('Listening for input...')
                    try:
                        _data = conn.recv(SOCKET_BUF_SIZE)
                        if not _data:
                            break
                        data = _data.decode().strip()
                        if data == '':
                            conn.send(b'x\n')
                            break
                        Log.dbg(f'Read: {data}')
                        conn.send(b'...')
                        yield conn, data
                    except ConnectionResetError:
                        break
            except Exception:
                Log.err('Connection interrupted', bail=False)
                continue
            finally:
                Log.dbg(f'Closed connection to: {addr[0]}:{addr[1]}')
