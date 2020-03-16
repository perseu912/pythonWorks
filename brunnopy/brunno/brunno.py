#Reinan Br.  20:39  07/01/2020

import numpy as np
from mpmath import *
from scipy import special

mp.pretty = True

#serie harmonica
H = harmonic
#constante de EulerMasqueroni
y = euler

#funcoes especiais

#função erro de Gauss
def erroGauss(x):
	return (2/pi**(1/2)*(quad(lambda t:(e**(-t**2)),[0,x])))

#funcao zeta de Riemman
def riemman(s):
	return 1+nsum(lambda u:(power(-log(u),u)*power(s,u)*(1/gamma(u+1))),[1,inf])

#funcao zeta de Dirichet
def dirichet(s):
	return nsum(lambda n:(power(-1,n)*power(2*n+1,-s)),[0,inf])

# intelgral de eulermasqerony gamma incompleta
def eulermasc(a,x):
	return quad(lambda t:exp(-t)*power(t,a-1),[0,x])
	
#funcao de eta dirichlet
def eta(s):
	return (nsum(lambda u: power(-1,u+1)/power(u,s),[1,inf]))

#funcao transcendental de lerch
def lerch(z,s,a):
	return nsum(lambda n:power(z,n)/power(n+a,s),[0,inf])

#funcao zeta de hurwitz
def hurwitz(s,q):
	return nsum(lambda k:1/power(k+q,s),[0,inf])

#funcao Polilogaritma
def L(s,z):
	return nsum(lambda k:power(z,k)/power(k,s),[0,inf])
	
#integral de euler-maskeroni
def em(n,z):
	return quad(lambda t:exp(t*n)/power(t,n),[0,inf])

#funcao de Hermite
def hermite(n,x):
	return (power(-1,n)*exp(power(x,2))*diff(lambda u:(exp(power(-u,2))),x))

#dfrac
def difrac(fun, x, n=1/2):
	iii = lambda s:(quad(lambda t:(fun(t)/power((s-t),n)),[0,s]))
	return (1/gamma(1-n))*diff(iii ,x)

#serie de maclaurin
def mac(s):
	n = 0
	for i in range(1,1000):
		n+=(s)**i/fat(i)
	return n
	
'''
if __name__ == '__main__':
	print(atez(7))
'''



