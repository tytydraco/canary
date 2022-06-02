#!/usr/bin/env bash;

CRON_PATH="/etc/cron.d/periodic_reboots"
CRON_CONTENT="0 3 * * * root /sbin/shutdown -r now"

echo "*** SETUP PERIODIC REBOOTS ***"

if [[ "$EUID" -ne 0 ]]
then
  echo "Not root! Exiting."
  exit
fi

if [[ ! -f "$CRON_PATH" ]]
then
  echo "*** ADDING CRON ENTRY TO $CRON_PATH"
  echo "*** $CRON_CONTENT"
  echo "$CRON_CONTENT" > "$CRON_PATH"
fi
