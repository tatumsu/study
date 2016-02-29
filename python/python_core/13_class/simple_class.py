class RoundFloat(object):
	def __init__(self, val):
		assert isinstance(val, float), \
		"Value must be a float!"
		self.value = round(val, 2)

	def __str__(self):
		return '%.2f' % self.value

	__repr__ = __str__


class Time60(object):
	'Time60 - track hours and minutes'

	def __init__(self, hr, min):
		'Time60 constructor - takes hours and minutes'
		self.hr = hr
		self.min = min

	def __str__(self):
		'Time60 - string representation'
		return '%02d:%02d' % (self.hr, self.min)

	__repr__ = __str__

	def __add__(self, other):
		'Time60 - overloading the addition operator'
		min = self.min + other.min
		hr = self.hr + other.hr
		if (min >= 60):
			hr += 1
			min = min % 60
	
		return self.__class__(hr, min)

	def __iadd__(self, other):
		'Time60 - overloading in-place addition'
		self.hr += other.hr
		self.min += other.min
		if (self.min >=60):
			self.hr += 1
			self.min = self.min % 60
		return self


class NumStr(object):

	def __init__(self, num=0, string=''):
		self.__num = num
		self.__string = string

	def __str__(self):		  
		# define for str()
		return '[%d :: %r]' %  self.__num, self.__string)
	__repr__ = __str__

	def __add__(self, other):	  
		#define for s+o
		if isinstance(other, NumStr):
			return self.__class__(self.__num + other.__num,  self.__string + other.__string)
		else:
			raise TypeError, 'Illegal argument type for built-in operation'

	def __mul__(self, num):		 # define for o*n
		if isinstance(num, int):
			return self.__class__(self.__num * num
				self.__string * num)
		else:
			raise TypeError, 'Illegal argument type for built-in operation'

	def __nonzero__(self):		  # False if both are
		return self.__num  or len(self.__string)

	def __norm_cval(self, cmpres):# normalize cmp()
		return cmp(cmpres, 0)

	def __cmp__(self, other):	  # define for cmp()
		return self.__norm_cval(
			cmp(self.__num, other.__num)) + self.__norm_cval(
			cmp(self.__string, other.__string))
