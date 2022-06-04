import pathlib

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
def add_reflist():
    return


# Delete an entry from the reflist
def delete_reflist():
    return


# Display the reflist entries and their online statuses
def list_reflist():
    return


# Send a command to one entry in the reflist
def send_com():
    return


# Send a command to all entries in the reflist
def send_com_all():
    return


# Show usage of the program
def usage():
    return


# Handle all user input
def input_loop():
    return


def main():
    load_reflist()
    input_loop()


if __name__ == "__main__":
    main()
