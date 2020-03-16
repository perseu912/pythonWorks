from Math.Brunno import *
from Math.MethodsNumeric import *


f = lambda x:(x**2)

dy = lambda x,y : 1-x+4*y
print(Euler(dy,10,0.1).listy)
print(Euler(dy,10,0.1).listx)

r = NewtonRaph(f,5)


print(f' eta {eta(2)}')
print(f'euler {eulermasc(2)}')
print(r.n)
print(f(r.x))
print(r.error)
print(zeta(2))
print(dirichet(2))
print(hermite(2,2))
f = lambda x: x
print(difrac(f,4))
#print(gamma(0))
'''
plt.plot(r.xlist,r.n)
plt.ylabel('error')
plt.show()
'''