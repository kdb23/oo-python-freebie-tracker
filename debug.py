import ipdb
from lib import *

c1 = Company("Blistex", 1964)
c2 = Company('Facebook', 2009)
d1 = Dev("Mad Max")
f1 = Freebie("Chapstick", 1, c1, d1)
f2 = Freebie("T-shirt", 1, c2, d1)



ipdb.set_trace()