#!/usr/bin/env python

'''CREATE TEXT FILE BY USER'S INPUT'''

import os
ls = os.linesep

# get filename
fname = raw_input('Enter file name: ')
while True:
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else:
        break

#get file content lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line seperator
file = open(fname, 'w')
file.writelines(['%s%s' % (x, ls) for x in all])
file.close()
print 'DONE!'
