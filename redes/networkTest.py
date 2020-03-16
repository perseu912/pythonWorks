#Reinan Br. 12:20 29/02/2020
import networkx as nx
import matplotlib.pyplot as plt
import random

#importando os dados
from data import *

g = nx.Graph()

#adicionando nós dos bairros
for i in range(len(alunos)):
	#print(alunos[i][1])
	g.add_node(alunos[i][0],pos=alunos[i][1])

#adicionando escola
g.add_node(escola,pos=(3,3))

#criando os laços com a escola
for i in range(len(alunos)):
	g.add_edge(alunos[i][0],escola,weight=random.random())

w = nx.get_edge_attributes(g, 'weight')
pos = nx.get_node_attributes(g, 'pos')

plt.figure()
nx.draw(g, pos,with_labels=True, egde_labels=w)
plt.show()