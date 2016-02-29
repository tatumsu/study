import redis
import random

REDIS_HOST = 'localhost'
KEY_SIZE = 50000
LIST_SIZE = 50000
PHONE_BASE = 13800000000

class User:
	"""Simple entitiy to represents an user"""
	def __init__(self, sid, name, age, email, telephone):
		self.sid = sid
		self.name  = name
		self.age = age
		self.email = email
		self.telephone = telephone

class DataGenerator:
	"""Provides to generate different redis object"""

	@staticmethod
	def generateHashmap():
		"""Generate a big keyspace with hashmap"""
		users = []
		r = redis.StrictRedis(host=REDIS_HOST)
		for i in range(KEY_SIZE):
			sid = i
			name = 'User:' + str(i)
			age = random.randint(20, 65)
			email = name + '@augmentum.com'
			telephone = PHONE_BASE + i

			key = 'user:' + str(sid)
			r.hset(key, 'sid', sid)
			r.hset(key, 'name', name)
			r.hset(key, 'email', email)
			r.hset(key, 'age', age)
			r.hset(key, 'telephone', telephone)

	"""Generate a big list"""
	@staticmethod
	def generateList():
		"""Generate a big keyspace with hashmap"""
		r = redis.StrictRedis(host=REDIS_HOST)
		for i in range(LIST_SIZE):
			r.lpush('list', i)


print(__name__)
if __name__ == '__main__':
	DataGenerator.generateList()
