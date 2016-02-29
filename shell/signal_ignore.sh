#!/bin/bash

trap 'echo SIGTSTP is received' SIGTSTP

echo "Sleep 10 seconds..."
sleep 10s

echo "Wakeup & Exit"
