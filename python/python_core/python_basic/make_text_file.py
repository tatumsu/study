#!/usr/bin/env python


'''make_text_file.py -- Create a text file based on user's input'''

import os
ls = os.linesep

file_name = raw_input('Enter the file name: ')
while True:
    if os.path.exists(file_name):
        print "ERROR: '%s' already exists" % file_name
    else:
        break

all = []
print "\n Enter lines ('.' by itself to quit).\n"

while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

file = open(file_name, 'w')
file.writelines(['%s%s' % (x, ls) for x in all])
file.close()
print 'DONE'
