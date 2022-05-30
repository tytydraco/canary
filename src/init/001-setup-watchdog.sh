#!/usr/bin/env bash;

echo "*** SETUP WATCHDOG ***"

if [[ "$EUID" -ne 0 ]]
then
  echo "Not root! Exiting."
  exit
fi

if ! grep -q "dtparam=watchdog=on" /boot/config.txt
then
  echo "*** ENABLING WATCHDOG IN BOOT CFG ***"
  echo 'dtparam=watchdog=on' >> /boot/config.txt
fi

if ! dpkg -s watchdog &> /dev/null
then
  echo "*** INSTALLING WATCHDOG PACKAGE ***"
  apt-get update
  apt-get install -y watchdog

  {
    echo 'watchdog-device = /dev/watchdog'
    echo 'watchdog-timeout = 15'
    echo 'max-load-1 = 24'
  } >> /etc/watchdog.conf
fi

echo "*** ENABLING WATCHDOG ON BOOT ***"
systemctl enable watchdog

echo "*** STARTING WATCHDOG ***"
systemctl start watchdog
