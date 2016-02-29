'READ FILE CONTENT'

print __name__

#get file name
fname = raw_input('Enter file name:')
print

#attemp to open file for reading
try:
    file = open(fname, 'r')
except IOError, e:
    print "*** Fail to open file:", e
else:
    #display content to screen
    for line in file:
        print line,
    file.close()


