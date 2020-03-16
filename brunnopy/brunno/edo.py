import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpmath import *

#função que retorna a taxa de variação da massa em relação ao tempo (dm/dt)
def edo(y,t):
	dydt = 1-y
	return dydt

#massa inicial
y0=2
m0=2

#tempo
t = np.linspace(0,10,100)

#gráfico que encontra a solução
y = odeint(edo,y0,t)

#solução real
m = 1-(1-m0)/e**t

#erro é zero
erro = (y-m)

#Plotagem do gráfico
plt.plot(t,m)
plt.plot(t,y,'--r')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
