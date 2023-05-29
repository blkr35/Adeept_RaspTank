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
  *)
    ;;
esac
exit 0

