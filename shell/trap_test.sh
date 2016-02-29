#!/bin/bash

file=/tmp/rap54ibs2sap.txt
trap "rm $file; echo I will leave; exit" 0 1 2 3 15
rm $file
