def foo():
    print "\ncalling foo()..."
    print "before assignment, bar is %s" % bar
    #global bar 
    bar = 200
    print "in foo(), bar is, %s, id(bar) is %s" % (bar, id(bar))
bar = 100
print "in __main__, bar is", bar
foo()
print "\nin __main__, bar is (still) %s, id(bar) is %s" % (bar, id(bar))

