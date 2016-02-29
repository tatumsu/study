import re

f = open('data.txt')
for line in f.readlines():
	print line,
	m = re.match(".+?(?P<number>\d+-\d+-\d+)", line)
	if m is not None:
	    print m.group('number')
