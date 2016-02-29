class Person(object):
    """Tatum's 1st class"""

    version = 0.1

    def __init__(self, name="tatum", age=35):
        """Constructor"""
        self.name = name
        self.age = age
        print "Person: [name]=%s,[age]=%d is created" % (name, age)

    def displayName(self):
        print "My name is: ", (self.name)
        print "My class name is: %s" % (self.__class__.__name__)

tatum = Person()
tatum.displayName()
print "My id is:", id(tatum)

aaron = Person("aaron", 31)
aaron.displayName()

print "Show object attributes"
print dir(tatum)

print "Show object documentation"
print help(tatum)
