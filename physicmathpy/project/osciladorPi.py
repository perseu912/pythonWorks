import matplotlib.pyplot as plt
import numpy as np

x =[]
y=[]
i = 0
#criador dos 100 primeiros termos
for n in range(100):
	i += 4*(((-1)**n)/(2*n+1))
	x.append(n)
	y.append(i)

#plotagem
plt.plot(x,y)
plt.ylabel('pi')

plt.show()
