#!/usr/bin/expect
set timeout -1

set password [lindex $argv 0]
set cmd [lrange $argv 1 end]

eval spawn $cmd
expect {
  "(yes/no)?"
  {
    send "yes\n"
    expect "*assword*:" { send "$password\n"}
  }
  "*assword*:"
  {
     send "$password\n"
  }
}
interact
