# canary
A Raspberry Pi maintenance utility

# Installation
- Clone canary to `/root/canary/`
- `cp /root/canary/canaryd.service /etc/systemd/system/ && chmod +x /etc/systemd/system/canaryd.service && systemctl enable --now canaryd`

# Communication
To send commands to an active canary server, communicate over TCP using the port specified in `src/other/config.py`. The simplest way to do this is via `nc` on a Linux machine.

`echo '<command>' | nc <ip> <port>`

# Usage
Commands are designed to be immutable, meaning that clients should not be able to specify extrenuous infrmation to the server aside from the base commands. No arguments may be specified. No output can be received.

- `reboot`: Reboot the server device
- `upgrade`: Run a full system upgrade via `apt-get`
- `ping`: Empty command; responds w/ positive acknowledgement

# Init
Canary bundles in a tiny init script helper. Scripts are executed every time canary starts up. Scripts MUST have execution permissions.

- `001-setup-watchdog.sh`: Setup and install the Linux Kernel watchdog program to automatically reboot on system freezes
- `002-setup-periodic-reboots.sh`: Automatically reboot the pi at 3:00 AM via a crontab entry

# Security
While convenience and accessibility is essential, security cannot be sacrificed. Canary is designed to keep a one-way stream of information. That means that no output can ever be returned to the client. The client is not allowed to specify any external information to the server for interpreting. Commands are not allowed to have arguments. There is no room for ambiguity.

# Configuration
See `src/other/config.py` for documentation.

# Client
You can use the built-in canary client called birdhouse to communicate with clients in a cleaner manner. It creates a file called `birdhouse` (not to be confused with `birdhouse.py`). It will get created automatically upon first launch of birdhouse.

The `birdhouse` file stores a list of references to canary clients. It uses the format `name:address:port`. Entries can be managed manually or via the `add` and `delete` commands.

Commands can be sent to individual entries or all of them at once.
