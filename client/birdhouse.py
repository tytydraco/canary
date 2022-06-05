import pathlib
import nmap
import socket

init_path = pathlib.Path(__file__).parent.resolve()
reflist_path = f'{init_path}/birdhouse'
pathlib.Path(reflist_path).touch()
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
    with open(reflist_path, 'r') as reflist_file:
        for raw_line in reflist_file.readlines():
            line = raw_line.strip()
            if line == '':
                continue
            name, address, port = line.split(':')
            reflist.append(RefEntry(name, address, int(port)))


# Add an entry to the reflist
def add_reflist(args):
    parts = ' '.join(args).split(':')
    if len(parts) != 3:
        print('bad entry')
        return False

    entry = RefEntry(parts[0], parts[1], parts[2])
    reflist.append(entry)
    update_reflist()
    return True


# Delete an entry from the reflist
def delete_reflist(args):
    name = ' '.join(args)
    finds = [entry for entry in reflist if entry.name == name]
    if len(finds) > 0:
        for find in finds:
            reflist.remove(find)
        update_reflist()
        return True
    else:
        print('no matches')
        return False


# Update the reflist file with the new data
def update_reflist():
    lines = [f'{entry.name}:{entry.address}:{entry.port}' for entry in reflist]
    with open(reflist_path, 'w') as reflist_file:
        for line in lines:
            reflist_file.write(line)
            reflist_file.write('\n')
        reflist_file.flush()


# Display the reflist entries and their online statuses
def list_reflist():
    scanner = nmap.PortScanner()
    for entry in reflist:
        print(f'{entry.name: <32}\t', end='')
        status = scanner.scan(entry.address, arguments='-v')
        online = status['nmap']['scanstats']['uphosts'] == '1'
        online_str = 'ONLINE' if online else 'OFFLINE'
        print(online_str)


# Send a command to one entry in the reflist
def send_com(args):
    name = args[0]
    command = ' '.join(args[1:])
    finds = [entry for entry in reflist if entry.name == name]
    if len(finds) > 0:
        find = finds[0]
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            soc.connect((find.address, find.port))
        except socket.error as message:
            print(f'connect failed: {message}')
            return False
        try:
            soc.send(command.encode())
        except BrokenPipeError:
            print(f'failed to send message')
            return False
        out = soc.recv(1024).decode()
        print(out)
        soc.close()
    else:
        print('no matches')
        return False


# Send a command to all entries in the reflist
def send_com_all(args):
    for entry in reflist:
        send_com([entry.name, " ".join(args)])


# Show usage of the program
def usage():
    print('exit: close the program')
    print('add <name>:<address>:<port>: add an entry')
    print('delete <name>: delete an entry')
    print('list: list all entries')
    print('send <name> <command>: send command to one entry')
    print('sendall <command>: send command to all entries')
    print('help: show list of commands')


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
