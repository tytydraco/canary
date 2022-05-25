from src.net.sockets import Sockets
from src.parser.parser import Parser


def main():
    sockets = Sockets()
    sockets.initialize()

    for command in sockets.read():
        Parser.handle_command(command)


if __name__ == "__main__":
    main()
