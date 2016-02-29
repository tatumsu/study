import sys

from importee import users, show

show()
users[1]='kaden'

print "In importer.py, users are:",
for user in users:
	print user,
print "\n", "-"*50
show()

print "Module load path:"
for path in sys.path:
	print path

print "\n", "-"*50
print "Loaded Modules:"
for module in sys.modules:
	print module
