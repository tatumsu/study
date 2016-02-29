from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.skip_bad_hosts=True
# env.hosts=['localhost'] 
env.user = "vagrant"
env.hosts = ['tatum@192.168.0.107:22','localhost']
# env.hosts.extend(['host3', 'host4'])
env.passwords={'tatum@192.168.0.107:22': 'abc123_', 'vagrant@localhost:22': 'vagrant'}
# env.roledefs['webservers'] = ['www1', 'www2', 'www3']

def get_host_spec():
  get_cpu()
  get_memory()
  get_disk()
 
def get_cpu():
  print("Executing on %(host)s as %(user)s" % env)
  with hide('stderr','running'):
    run("echo $(lscpu | grep 'CPU(s):')")
  # print env.passwords 

def get_memory():
  with hide('stderr','running'):
    run("echo $(free -m | grep Mem: | tr -s ' ' | cut -d ' ' -f2 | xargs echo 'Total Memory: ')")
 
def get_disk():
  with hide('stderr','running'):
    run("df -h")
 
def handle_error():
  with settings(warn_only=True):
    result = run("ls /tmp/notexist")
  if result.failed and not confirm("Command failed. Continue anyway?"):
    abort("Aborting at user request.")
  # The shell is an empty shell
  with cd('/vagrant'):
    run('env && alias')
    run('type ls')

@hosts('localhost')
def run_local():
  run('whoami')
  print env.connection_attempts
