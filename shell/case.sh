#!/bin/bash

read -p  "Input your age: " age
echo "You age is $age"

case "$age" in
[1-9]) echo "Your age is below 10"
    ;;& # Evaluate the next condition and execute if valid
4) echo "You are still yong"
    ;& # continue the next command
5) echo "You are matural enough"
    ;;
*) echo "You are old"
    ;;
esac
