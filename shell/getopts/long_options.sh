#!/bin/bash -e
# parse-long-options-arguments.sh

# Set a constant to hold the number of mandatory arguments
declare -r mandatory=3

basename=`basename $0`

# Use HEREDOC for multi line output. Note the backstick in a line after the closing EOF. You can include any type of quotation inside HEREDOC.
usage_text=`cat <<EOF
usage: $basename 
  --option1  Option #1
  --option2  Option #2
  --option3  Option #3
EOF
`
# Use the HEREDOC defined variable from a function that exits with a non zero code indicating failure
usage() {
 echo "$usage_text";
 exit 1;
}

# Loop through arguments thanks to shell exapansion builting "a colon". Avoid repetition using declare
argc=0
while :
do
        case $1 in
                --option1|\
                --option2|\
                --option3) var=${1:2}; shift; val=$1; shift; declare "$var=$val"; argc=$[$argc + 1];;
                *) if [[ ! -z $1 ]]; then usage; fi; break;;
        esac
done

# Check that mandatory parameters have been supplied
if [ $argc -ne $mandatory ]; then
  usage;
fi

# Sample output to illustrate this actually works
echo  "option1=$option1 option2=$option2 option3=$option3"
