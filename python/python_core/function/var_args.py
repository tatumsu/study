def foo(arg1, arg2='defaultB', *theRest):
    'display regular args and non-keyword variable args'
    print 'formal arg 1:', arg1
    print 'formal arg 2:', arg1
    for eachXtrArg in theRest:
        print 'another arg:', eachXtrArg

foo(1, 2, 3, 'tatum')
foo(1, 'a', 'bc', 'this', 'rest')

