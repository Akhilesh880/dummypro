import random
from random import *

l=[ i for i in range(0,21)]
shuffle(l)
print(l)
#a=shuffle(l)
for i in l:
	shuffle(l)
	print(i)
