#author => Jezuis_Matrix 11:50 30/9/2019
 
import mechanicalsoup
from bs4 import BeautifulSoup as bs
import requests
import json
import random
 
 
#instância o browser com as requisições basicas
class Browser:
	def __init__(self, http=None, https=None, agent=None):
		br = mechanicalsoup.StatefulBrowser()
		if(https and agent):
			try:
				proxies = {'http':http ,'https':https}
				agent = {'agent':agent}
				br.session.proxies = proxies
				br.session.proxies.update(proxies)
				br.session.headers = agent
				br.session.headers.update(agent)
				print('browser configurado com as proxy instanciado com sucesso')
			except:
				print('ops, ocorreu um erro, verifique suas configurações e tente novament')
				exit()
		self.br = br
		print('browser instanciado')
		
	
	#abre o site 
	def open(self, url, prnt=False):
		res = self.br.open(url)
		self.reqest = True
		if(prnt):
			re = self.br.get_current_page()
			print(re)
		return res
		
	#retorna um elemento especifico
	def getElement(self, element)
	
	#trabalha os form da pagina
	def form(self, nameForm, nameInput, input):
		self.form = self.br.select_form(f'form[name="{nameForm}"]')
		self.form.set(nameInput, input)
		
	def sendForm(self):
		res = self.br.submit_selected()
		return res
 
 
 #### procura uma proxy valida ####
 
 #retorna proxie type https
def https():
	urlHttps= 'https://www.proxy-list.download/api/v1/get?type=https&anon=elite&country=US'
	proxiesHttps = (requests.get(urlHttps).text).split()
	#print(proxies)
	return proxiesHttps[random.randint(0,len(proxiesHttps))]
	
#print(https())
 
 
def http():
 	urlHttp = 'https://www.proxy-list.download/api/v1/get?type=http&anon=elite&country=US'
 	proxiesHttp = (requests.get(urlHttp).text).split()
 	return proxiesHttp[random.randint(0,len(proxiesHttp))]
 # fazendo o request do site de proxies


