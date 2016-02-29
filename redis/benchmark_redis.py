import os
import redis
import random
import string
import time
from multiprocessing import Process, Value, Array
from datetime import datetime

REDIS_HOST = 'localhost'
PROCESS_NUMBER = 1
r = redis.StrictRedis(host=REDIS_HOST)

TEST_RUN = Value('d', 0.0)

def bench(desc, count, f): 
	start = datetime.now()
	TEST_RUN = Value('d', 0.0)
	processes = []
	for i in range(0, PROCESS_NUMBER):
		p = Process(target = f, args=(count,))
		processes.append(p)
		p.start()
		
	for p in processes:
		p.join()

	seconds  = (datetime.now() - start).seconds
	print("Benchmark %s (%d): %s seconds" % (desc, count, seconds))


def random_str(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def without_pipelining(count):
	pipe = r.pipeline()
	for i in range(0, count):
		pipe.ping()
	pipe.execute()


def with_pipelining(count):
	for i in range(0, count):
		r.ping()


def test_get(count):
	for i in range(0, count):
		ri = random.randint(0, count)
		r.get(str(ri))


def test_hget(count):
	for i in range(count):
		ri = random.randint(0, count)
		address = r.hget('addrss:' + str(ri), 'address')


def test_set(count):
	r = redis.StrictRedis(host=REDIS_HOST)
	for i in range(0, count):
		#s = str(i) + random_str(10)
		r.set(str(i), random_str(10)) 
		TEST_RUN.value = TEST_RUN.value + 1
		#print('process %d with run=%d:' % (os.getpid(), TEST_RUN.value))
		#time.sleep(5)
		if (TEST_RUN.value >= count):
			break


#bench("SET", 500000, test_set)
bench("GET", 500000, test_get)
#bench("HGET", test_hget)
