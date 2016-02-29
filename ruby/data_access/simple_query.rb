require 'pg'

options = { 
  :host=>'192.168.0.110',
  :dbname=>'victory_packaging',
  :user=>'postgres',
  :password=>'abc123_'
}
conn = PG.connect(options)
rows = conn.exec('SELECT sid, driver_id FROM ods.common_entities_driver LIMIT 3;')
puts "PID=#{$$}"
rows.each { |row|
  puts "SID=#{row['sid']}, DRIVER_ID=#{row['driver_id']}";
  sleep(35)
  exit 0;
}
exit 0;
