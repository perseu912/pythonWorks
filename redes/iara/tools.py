#Reinan Br. 10:05 29/02/2020

from random import choice
import random
import psutil as ps

#cpu = ps.cpu_percent()
cpu = ps.virtual_memory()
#print(cpu)
numberCpu = ps.cpu_count()
#print(numberCpu)
freqCpu = ps.cpu_freq(percpu=True)
#print(freqCpu)

