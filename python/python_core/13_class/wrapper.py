class WrapMe(object):
	def __init__(self, obj):
		self.__data = obj
	
	def get(self):
		return self.__data
	
	def __repr__(self):
		print '__repr__ is invoked'
		return 'self.__data.real.x'
	
	def __str__(self):
		print '__str__ is invoked'
		return str(self.__data)
	
	def __getattr__(self, attr):
		print '__getattr(%s)__ is invoked' % attr
		return getattr(self.__data, attr)

	def __getattribute__(self, attr):
		print '__getattribute(%s)__ is invoked' % attr
		return super(WrapMe, self).__getattribute__(attr)


wrappedComplex = WrapMe(3.5+4.2j)
wrappedComplex                #a   wrapped object: repr()
print wrappedComplex.real           # real attribute
print wrappedComplex.imag           # imaginary attribute
print wrappedComplex.conjugate()    # conjugate() method
wrappedComplex.get()          # actual object

