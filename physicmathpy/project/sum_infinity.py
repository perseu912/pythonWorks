
from mpmath import *
mp.dps = 100
   
'''x = symbols('x')

i = limit(((-1)**x)/(1+2*x)**3, x, oo)
    

'''
#soma infinita
r = nsum(lambda x:((-1)**x/(1+2*x)**3),[0,inf])
print(r)

rr = nsum(lambda x: (1/2**x), [0, inf])

print((32*r)**(1/3))
print(rr)


ee = nsum(lambda x: (1/fac(x)), [0, inf])
print(ee)