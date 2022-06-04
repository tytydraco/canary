import pathlib
import nmap

init_path = pathlib.Path(__file__).parent.resolve()
reflist_path = f'{init_path}/birdhouse'
pathlib.Path(reflist_path).touch()
reflist_file = open(reflist_path, 'r+')
reflist = []


class RefEntry:
    name = ''
    address = ''
    port = 0

    def __init__(self, name, address, port):
        self.name = name
        self.address = address
        self.port = port


# Parse data from the reflist file into an actual list
def load_reflist():
    for line in reflist_file.readlines():
        name, address, port = line.split(':')
        reflist.append(RefEntry(name, address, port))


# Add an entry to the reflist
def add_reflist(args):
    return


# Delete an entry from the reflist
def delete_reflist(args):
    return


# Display the reflist entries and their online statuses
def list_reflist():
    scanner = nmap.PortScanner()
    for entry in reflist:
        status = scanner.scan(entry.address, arguments='-v')
        online = status['nmap']['scanstats']['uphosts'] == '1'
        online_str = 'ONLINE' if online else 'OFFLINE'
        print(f'{entry.name: <32}\t{online_str}')


# Send a command to one entry in the reflist
def send_com(args):
    return


# Send a command to all entries in the reflist
def send_com_all(args):
    return


# Show usage of the program
def usage():
    return


# Handle all user input
def input_loop():
    while True:
        raw_command = input('> ')
        parts = raw_command.split(' ')
        command = parts[0]
        args = parts[1:] if len(parts) > 1 else None

        if command == 'exit':
            break
        elif command == 'add':
            add_reflist(args)
        elif command == 'delete':
            delete_reflist(args)
        elif command == 'list':
            list_reflist()
        elif command == 'send':
            send_com(args)
        elif command == 'sendall':
            send_com_all(args)
        elif command == 'help':
            usage()
        else:
            print('bad command; try "help"')


def main():
    load_reflist()
    input_loop()


if __name__ == "__main__":
    main()
