#Reinan_Santts 1/1/2020, 4:45

import random as rd
from mpmath import *
mp.pretty = True


def brutal(fun,n, error = 15):
	#definition of x0,y0
	x0 = 0
	y0 = 0
	
	#randing x,y
	x = (rd.randint(1,5))
	y = rd.randint(1,5)
	
	#first error is 0
	e = 0
	while(True):
		
		#diferenciation's of x,y
		hx = x - x0
		hy = y - y0
		
		#help-me in df (bug in 2 loop)
		#derive of fun in x,y
		df = diff(fun,(1,1),(x,y))
		
		#adj's of x,y
		adj_y = -(e/df+hy)
		adj_x = -(e/df+hx)
		
		#findroot
		y = abs(y0 + adj_y)
		x = abs(x0 + adj_x)
		
		# change the x0,y0
		x0 = x
		y0 = y
		
		#find error
		e = fun(x,y) - n 
		
		#if error ~ 0 stop
		if(e==10**(-error)):
			break
		
	return x
	
c = lambda x,y :power(power(x,2)+power(y,2),1/2)
print(c(4.0,3.0))
print(diff(c,(1,1),(2,4)))
print(brutal(c,2,1))