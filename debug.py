import ipdb
from lib import *

c1 = Company("Blistex", 1964)
c2 = Company('Facebook', 2009)
c3 = Company('IBM', 1919)

d1 = Dev("Mad Max")
d2 = Dev("Krazy Kim")


f1 = Freebie("Chapstick", 1, d1, c1)
f2 = Freebie("T-shirt", 12, d2, c2)



ipdb.set_trace()