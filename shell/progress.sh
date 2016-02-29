#!/bin/bash
# progressdots.sh - Display progress while making backup
# Based on idea presnted by nixCraft forum user rockdalinux
# Show progress dots

progress(){
  echo -n "$0: Please wait..."
  while true
  do
    echo -n "."
    sleep 2
done
}

dobackup(){
  # put backup commands here
  for i in {1..5}
  do
    sleep 5
  done
  # tar -zcvf /dev/st0 /home >/dev/null 2>&1
}
# Start it in the background
progress &
# Save progress() PID
# You need to use the PID to kill the function
MYSELF=$!
echo "Progress PID=$MYSELF"
trap "echo Killed && kill $! &>/dev/null; exit" SIGKILL SIGINT SIGTERM

# Start backup
# Transfer control to dobackup()
dobackup
# Kill progress
kill $MYSELF >/dev/null 2>&1
echo -n "...done."
echo
