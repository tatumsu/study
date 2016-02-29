#!/usr/bin/env python

import sys

print 'number of augmentum: %d' % len(sys.argv)
i = 0
# arev index start from 0
for arg in sys.argv:
	print 'sys.argv[%d] = %s' % (i, arg)
	i = i+1

