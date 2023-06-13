#! /bin/sh
# chkconfig: 345 99 10
case "$1" in
  start)
    # Executes our script
    sh /home/root/Adeept_RaspTank/startup.sh
    ;;
  stop)
    killall python3
    ;;
  status)
    if [ $(pidof python3) ]; then
        echo "RaspTank software is running"
    else
        echo "RaspTank software has stopped"
    fi
    ;;
  *)
    ;;
esac
exit 0

