m = re.match('(\w*\s)*(\w*foo)', 'this is seafood')
if m is not None:                      
    m.group()



m = re.search('foo', 'this is seafood')
if m is not None:                      
    m.group()
    
re.sub('PHONE', '13764803825', 'tatum phone number is: PHONE')    

import re
import os

os.system('who > /tmp/whodata.txt')
f = open('/tmp/whodata.txt', 'r')

for line in f.readlines():
    print re.split('\s\s+', line)
    

f.close()
