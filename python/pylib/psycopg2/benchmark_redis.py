import redis
import random
from datetime import datetime

REDIS_HOST = 'localhost'
r = redis.StrictRedis(host=REDIS_HOST)
count = 0


begin_time = datetime.now()
print("start test at: %s", str(begin_time))
for i in range(100000):
	ri = random.randint(500000, 600000)
	address = r.hget('addrss:' + str(ri), 'address')

end_time = datetime.now()
print("end test at: %s", str(end_time))
print("total time cost: %s", str(end_time - begin_time))

