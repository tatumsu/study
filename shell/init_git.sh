#!/bin/sh

# Generating the expect_pwd_exe.sh script
if [ -f expect_pwd_exe.sh ]
then
  rm -f expect_pwd_exe.sh
fi

(
cat <<'EOF'
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
EOF
) > ./expect_pwd_exe.sh

chmod +rx ./expect_pwd_exe.sh

CURRENT_USER=`id -un`
CURRENT_USER_HOME="/home/$CURRENT_USER"
GIT_SCP_PWD="abc123_"

## Get the current shell script dir
SHELL_SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

function show_progress()
{
  echo -e "\e[32m$1\e[0m"
}

pushd .

git --version || sudo yum -y install git

cd $CURRENT_USER_HOME
[ -d .ssh ] || mkdir .ssh
cd .ssh

# Copy xrs git deploy key to local and configure it with ssh
sudo yum -y install expect
$SHELL_SCRIPT_DIR/expect_pwd_exe.sh $GIT_SCP_PWD scp xrs_deploy@xrslxgit01.xata-aws.com:/home/xrs_deploy/xrs_git_deploy_id_rsa .
chmod go-r xrs_git_deploy_id_rsa
[ -f config ] || touch config
egrep "xrs_git_deploy_id_rsa" config || echo -e "Host xrslxgit01.xata-aws.com\n  IdentityFile ~/.ssh/xrs_git_deploy_id_rsa" >> config

sudo chown -R $CURRENT_USER .
chmod 0600 *
popd

show_progress "----Create /xrs/software and /xrs/deploy folder if not exist yet"
[ -d /xrs/software ] || sudo mkdir -p /xrs/software
[ -d /xrs/deploy ] || sudo mkdir -p /xrs/deploy
sudo chown -R $CURRENT_USER /xrs

pushd .
show_progress "Clone xrs_linux_init from GIT to local folder /xrs/deploy"
cd /xrs/deploy/
if [ -d /xrs/deploy/xrs_linux_init ]; then
  rm -rf /xrs/deploy/xrs_linux_init
fi
git clone "git@xrslxgit01.xata-aws.com:xrs-puppet/xrs_linux_init.git"

cd /xrs/deploy/xrs_linux_init
chmod +x *.sh

popd

