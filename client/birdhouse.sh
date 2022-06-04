#!/usr/bin/env bash

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]:-$0}")" &> /dev/null && pwd 2> /dev/null)"
REFLIST_PATH="$SCRIPT_DIR/birdhouse"

# Create the reflist file if it does not yet exist
prepare_reflist() {
  echo
}

# Parse data from the reflist file into an actual list
load_reflist() {
  echo
}

# Add an entry to the reflist
add_reflist() {
  echo
}

# Delete an entry from the reflist
delete_reflist() {
  echo
}

# Display the reflist entries and their online statuses
list_reflist() {
  echo # also ping them to show online status
}

# Send a command to one entry in the reflist
send_com() {
  echo
}

# Send a command to all entries in the reflist
send_com_all() {
  echo
}

# Show usage of the program
help() {
  echo
}
