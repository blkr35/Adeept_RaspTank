#!/bin/sh
ifup wlan0
if [ ! -f "/.rasptank_installed" ]; then
  echo "Update/Installation of software requested..."
  python3 //home/root/Adeept_RaspTank/setup.py
else
  echo "Software is already installed..."
fi 
python3 //home/root/Adeept_RaspTank/server/webServer.py
