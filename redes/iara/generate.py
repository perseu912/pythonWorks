#ReinanBr 21:43 26/02/2020

try:
	
	from iara.tools import *
except:
	from tools import *
	


v = ['a','e','i','o','u']
c = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','y','x','z']

#print(choice(c)+choice(v))

def nome(silabas=3):
	nome = []
	for i in range(silabas):
		nome.append(choice(c)+choice(v))
		
	return ''.join(str(x) for x in nome)
	
#print(nome())

def geraInt(i, f):
	return random.randint(i,f)
	
def geraConj(n=2):
	return geraInt(1,40),geraInt(1,40)
'''	
for i in range(100):
	print(nome(5))
'''
	