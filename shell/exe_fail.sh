#!/bin/bash

shopt -s execfail
echo "first line"
echo "try to execute a non-exist shell script"
#exec ./non_exist.sh
exec xyz

echo "i am still alive"
