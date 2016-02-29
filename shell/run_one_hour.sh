#!/bin/bash

echo "I am going to sleep for 1 hour"
echo "My PID=$$"
trap "echo SIGHUP is disbaled" SIGHUP SIGTERM SIGINT SIGSTOP
sleep 5m
