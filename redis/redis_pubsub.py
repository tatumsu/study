import redis

REDIS_HOST='192.168.184.99'
r = redis.StrictRedis(host=REDIS_HOST)
ps = r.pubsub()
ps.subscribe('room1')

for item in ps.listen():
	if item['data'] == "KILL":
		print("recevie KILL, exit")
		ps.unsubscribe()
	else:
		print(item['channel'], ":", item['data'])

