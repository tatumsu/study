class User(object):
	name='N/A'
	count = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
		count = count + 1

	def __getattribute__(self, attr):
		print "__getattribute__(self, %s) is invoked" % attr
		return super(User, self).__getattribute__(attr)

tatum = User('tatum', 35)
print tatum.name
print tatum.age
print User.count
tatum.email = 'tatum.su@augmentum.com'
