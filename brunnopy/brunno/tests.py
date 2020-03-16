from brunno import *
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 5, 10)
print(erroGauss(5))

erro = []
for n in range(t):
	erro.append(erroGauss(t[n]))
 

plt.plot(t,erro)
plt.xlabel('tempo')
plt.ylabel('erro de Gauss')
plt.show()
