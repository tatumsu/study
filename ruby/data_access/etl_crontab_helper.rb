# ------------------------------------------------------------------------------
# Author:           nick liu
# Create Date:      2014/10/21
# Description:      The base class for all deploy steps.
# ------------------------------------------------------------------------------

require 'pg'
require 'optparse'
require 'socket'

class ETLCrontabHelper

   @@etl_log_folder = "/var/log/xrs/etl"

   @@db_suite_query =<<-QUERY_STMT
      SELECT
        instance.server_name AS server_name,
        suite.name AS db_name
      FROM system_config.mstr_db_suite AS suite
      JOIN system_config.mstr_db_suite_to_mstr_db_instance AS sti
      ON suite.sid = sti.mstr_db_suite_sid
      JOIN system_config.mstr_db_instance AS instance
      ON sti.mstr_db_instance_sid = instance.sid
      WHERE suite.mark_for_delete = FALSE
      AND instance.mark_for_delete = FALSE
      AND instance.db_type = 5;
    QUERY_STMT

    @options = nil

   def execute(options)
     local_customer_databases = get_local_customer_databases(options)
     puts  local_customer_databases
     local_customer_databases.each { |database|
       execute_etl_job(database[:db_name])
     }
   end

  #
  # This method returns all customer databases on the local machine
  #
  def get_local_customer_databases(options)
    conn = PG.connect(options)
    all_customer_databases = []
    conn.exec(@@db_suite_query).each { |row|
      database = {}
      database[:server_name] = row['server_name']
      database[:db_name] = row['db_name']

      all_customer_databases.push(database)
    }
    conn.close

    local_customer_databases = all_customer_databases.select { |database|
       is_local_server?(database[:server_name])
    }
    local_customer_databases
  end


  def is_local_server?(db_server_name)
    if @local_ips == nil
      @local_ips = get_local_ips
    end
    db_server_ip = get_ip_address(db_server_name)
    result = @local_ips.include?(db_server_ip)
  end

  #
  # Spawn a process to execute ETL job for the specfiied database
  #
  def execute_etl_job(customer_db_name)

    # ensure_folder_exists etl_log_folder
    etl_shell_command = <<-SHELL_COMMAND
      psql \
      --host=127.0.0.1 \
      --dbname=#{database} \
      --username=xrs_crontab \
      --nopassword \
      --command="SELECT etl.fn_etl_controller()" \
      --log-file=#{@etl_log_folder}/run_etl_controller_#{customer_db_name}.log \
      --output=#{@etl_log_folder}/run_etl_controller_#{customer_db_name}.out \
      >> #{etl_log_folder}/run_etl_controller_#{customer_db_name}.txt 2>&1
    SHELL_COMMAND
    puts etl_shell_command
    spawn(etl_shell_command)
  end

  def get_ip_address(server_name)
    if server_name == nil || server_name == ""
      return ''
    else
    	list = Socket.getaddrinfo(server_name.to_s, nil, :INET)

    	if list.length >= 1
    		return list.last[2] # why?
    	else
    		fail("no ip found from server #{server_name}")
    	end
    end
  end

  def get_local_ips
    shell = ENV['SHELL']
    local_ips = nil
    if (shell.downcase.index('bin') > 0)
      local_ips = `/sbin/ifconfig`.scan(/inet addr:([\d\.]+)/).flatten
    else
      local_ips = `ipconfig /all`.scan(/inet addr:([\d\.]+)/).flatten
    end
    local_ips
  end
end

# define the default option values
options = {:port=>5432, :dbname=>'xrs_master', :user=>'xrs_crontab'}

option_parser = OptionParser.new do |opts|
  opts.banner = 'A small script to execute XRS ETL process'

  opts.on('-h HOST', '--hostname HOST', 'The master database host. This parameter is required.') do |value|
    options[:host] = value
  end

  opts.on('-p PORT', '--port PORT', 'Master database port number. The default value is 5432.') do |value|
    options[:port] = value
  end

  opts.on('-d DB', '--dbname DB', 'Master database name, The default value is xrs_master.') do |value|
    options[:dbname] = value
  end

  opts.on('-U USER', '--username USER', 'Name of the database user under which ETL database operation is performed.',
    'The default value is xrs_crontab') do |value|
    options[:user] = value
  end

  opts.on_tail('-?', "--help", "Show this message") do
    puts opts
    exit
  end
end.parse!

etlCrontabHelper = ETLCrontabHelper.new()
etlCrontabHelper.get_local_customer_databases(options)
#etlCrontabHelper.execute(options)