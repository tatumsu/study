class User(object):
	def __init__(self, name, password, age, email, mobile_phone):
		self.name = name
		self.email = email
		self.mobile_phone = mobile_phone
		self.age = age
		self.password = password
		print "User %s is created" % self.name


	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_password(self):
		return self.password

	def __del__(self):
		#object.__del__(self)
		print "User %s is deleted" % self.name

