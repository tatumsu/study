def test():
    import time
    try:
        time.sleep(10)
    except (KeyboardInterrupt, SystemExit): # chile of BaseExcpetion
        print "KeyboardInterrupt is caught"
    except Exception, e:
        print e
    
    print "Exit"


# - BaseException
#   |- KeyboardInterrupt
#   |- SystemExit
#   |- Exception
#      |- (all other current built-in exceptions)
# 

test()
