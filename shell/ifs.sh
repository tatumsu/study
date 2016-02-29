#!/bin/bash

pwd="tatum:x:102:102::/home/tatum:/bin/sh"
old="$IFS"
IFS=:
read -r login password uid gid info home shell <<< "$pwd"
printf "Your login name is %s, uid %d, gid %d, home dir set to %s with %s as login shell\n" $login $uid $gid $home $shell
IFS="$old"
