#!/bin/sh
ifup wlan0
if [ ! -f /.rasptank_installed ]
  echo "Update/Installation of software requested..."
  python3 //home/root/Adeept_RaspTank/setup.py
fi 
python3 //home/root/Adeept_RaspTank/server/webServer.py
