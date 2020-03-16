import matplotlib.pyplot as plt
import numpy as np
from mpmath import *

def zeta_graf(n=(-2), lim=(100)):
	x = []
	y = []
	l = np.linspace(1, lim, lim)
	for i in l:
		f = (-1)**i/(i**n)
		y.append(f)
		x.append(i)
		
	plt.plot(x,y)
	plt.xlabel('termos n')
	plt.ylabel('zeta f')
	plt.show()
	
#zeta_graf((-20))


mp.dps = 12

def catalan(s):
	return nsum(lambda x:((-1)**x*(2*x+1)**(-s)),[0, inf])
	
b = catalan(2)
print(b)