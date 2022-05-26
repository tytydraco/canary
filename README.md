# canary
A Raspberry Pi maintenance utility

# Installation
TODO

# Communication
To send commands to an active canary server, communicate over TCP using the port specified in `src/other/config.py`. The simplest way to do this is via `nc` on a Linux machine.

`echo '<command>' | nc <ip> <port>`

# Usage
Commands are designed to be immutable, meaning that clients should not be able to specify extrenuous infrmation to the server aside from the base commands. No arguments may be specified. No output can be received.

- `reboot`: Reboot the server device
- `upgrade`: Run a full system upgrade via `apt-get`

# Init
Canary bundles in a tiny init script helper. Scripts are executed every time canary starts up.

- `001-setup-watchdog.sh`: Setup and install the Linux Kernel watchdog program to automatically reboot on system freezes

# Security
While convenience and accessibility is essential, security cannot be sacrificed. Canary is designed to keep a one-way stream of information. That means that no output can ever be returned to the client. The client is not allowed to specify any external information to the server for interpreting. Commands are not allowed to have arguments. There is no room for ambiguity.

# Configuration
See `src/other/config.py` for documentation.
