from mpmath import *

def catalan(s, d=100):
	mp.dps = d
	return nsum(lambda x:((-1)**x*(2*x+1)**(-s)),[0, inf])
	
b = catalan(2, 200)
print(b)