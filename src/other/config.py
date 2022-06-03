import os

# Should we print debug information?
DEBUG = True

# Should be execute the init scripts?
INIT = False

# TCP port to listen on
LISTEN_PORT = 6543

# Size in bytes for the buffer for each socket read
SOCKET_BUF_SIZE = 1024

# Log all output to a file
LOGGING = True

# Log file directory location
LOG_FILE_DIR_PATH = f'{os.getenv("HOME")}/canary_logs'
