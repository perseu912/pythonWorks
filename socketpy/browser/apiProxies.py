import requests
from bs4 import BeautifulSoup as bs
import json


#url da api
urlProxies1 = bs(requests.get('https://sockslist.net/').text, 'lxml')

#organizando as proxies
n = urlProxies1.find_all('td')
proxielist =[]
for i in n:
	try:
		proxielist.append(i.contents[0].text+':'+i.contents[1].text)
	except:
 		break

print(proxielist)
 
 
 ###########################
#test url's
urlApi1 = 'http://pubproxy.com/api/proxy'
urlApi2 = ('https://api.getproxylist.com/proxy')
urlApi3s = 'https://www.proxy-list.download/api/v1/get?type=https&anon=elite&country=US'

#inicia o objeto Api de proxy 
class Api:
	def __init__(self):
		api = requests.get(urlApi1)
		self.api = json.loads(api.text)['data'][0]
		print(self.api)
		#self.port = self.api['port']
		self.ip = self.api['ipPort']
		self.protocol = self.api['type']

#busca pelo proxy com protocolo http
def http():
	res = ''
	while(True):
		api = Api()
		if(api.protocol == 'http'):
			res = api
			break
		else:
			continue	
	return res

#busca pelo proxy com protocolo socks
def https():
	res = ''
	while(True):
		api = Api()
		if(api.protocol != 'http'):
			res = api
			break
		else:
			continue	
	return res
	
######################

