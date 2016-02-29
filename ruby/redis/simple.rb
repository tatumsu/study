require 'rubygems'
require 'redis'
reids = Redis.new

redis = Redis.new(:host=>'127.0.0.1', :port=>6379)
redis.set('hello', 'world')
puts redis.get('hello')
puts redis.hget('book:5', 'title')
