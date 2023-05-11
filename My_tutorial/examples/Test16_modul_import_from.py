import time
import os
import random as r
import modul
from modul import add

try:
    import nomodul
except ImportError:
    print(' No moduls')

print (time.time())
print (os.getcwd())
print (r.random()*100)

modul.hi()
print (modul.add(45, 15))

print (add(67,123))



