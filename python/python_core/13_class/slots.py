class User(object):
	__slots__ = ('name', 'age')

	def __init__(self, name, age):
		self.name = name
		self.age = age

	
tatum = User('tatum', 35)
tatum.email = 'tatum.su@augmentum.com'
print tatum
