#!/bin/bash
#set -o posix
#set -o errexit
echo "sub shell option"
echo "-----------------------------------------------------------------------------------"
set -o
echo "-----------------------------------------------------------------------------------"
#echo "An error in command subsistition will be ignored when shell is NOT in posix mode"
(echo "command grou"; set -o; error)

echo "There is an error in sub shell"
echox "I am bad"
echo "I am still alive after the error in sub.sh"
