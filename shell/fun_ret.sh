#!/bin/bash

test()
{
  #echo "In function $FUNCNAME"
  rm $1  
  return 3
}

test $1
echo "Function test() return value:  $?"
test not_exits.txt
echo "Function test() return value:  $?"

