#Reinan Br. 18:46 29/02/2020

import networkx as nx

#metódo redes no formato mapa
class netMap:
	def __init__(self,data):
		#verificando se a data está no formato requerido
		self.g = nx.Graph()
		self.node = []
		self.pos = []
		try:
		
			for i in range(len(data)):
				self.node.append(data[i][0])
				self.pos.append(data[i][1])
				
				self.g.add_nodes(self.node[i],pos=self.pos[i])
				
		except:
			raise Exception('a data de nó implementada não está no formato aceito: a data que deve ser implementada deve ser no formato array [[nome_nó1,posição_nó1(x,y)],[nome_nó2,posição_nó2(x,y)] ...]')
		
	def Distance(self,node1,node2,i=0):
		try:
			a1 = node1[i][1][0]
			b1 = node1[i][1][1]
			
			a2 = node2[i][1][0]
			b2 = node2[i][1][1]
			
			dis =((a1-a2)**2+(b1-b2)**2)**(1/2)
			return dis
			
		except:
			raise Exception('a data de nó implementada não está no formato aceito: a data que deve ser implementada deve ser no formato array [[nome_nó1,posição_nó1(x,y)],[nome_nó2,posição_nó2(x,y)] ...]')
		
	def weighing(self):
		
			

i=[['pau',(2,4)]]
m = netMap(i).pos			