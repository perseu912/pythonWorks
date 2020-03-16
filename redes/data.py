#import tools.geoCoord as geo
import iara.generate as gera


#print(gera.nome(5))



escola = 'if-sertao'

alunos = [
			['joao',(2,5)],
			['thiago',(4,5)],
			['bernado',(4,5.5)],
			['vitor',(3,4.4)],
			['henrique',(7,6)],
			['vanderlei',(2,1)]
		]

		
for i in range(100):
	alunos.append([gera.nome(5),gera.geraConj()])
	
#print(alunos)
