require 'active_record'
require 'pg'


class Customer < ActiveRecord::Base
  #set_table_name "customer"
  #set_primary_key "sid"
end

ActiveRecord::Base.establish_connection(
  :adapter => "postgresql",
  :host => "localhost",
  :username => "vagrant",
  :password => "abc123_",
  :database => "tatum")

tatum = Customer.new
tatum.user_name='tatum'
tatum.first_name='tatum'
tatum.last_name='su'
tatum.email='tatum.su@augmentum.com'
tatum.age=35
tatum.description='good person'
tatum.save
