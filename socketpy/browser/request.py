#Reinan Br. 21/57 04/03/2020

import requests as rq
from bs4 import BeautifulSoup as bs
import wget


class Link:
	def __init__(self, link):
		self._link = link
		
	def download(self, title=None):
		nameFile = title if title else self.link
		'''try:
			
			file = rq.get(self._link)
			f = open(nameFile,'wb+')
			f.write(file)
			#f.close()
			
			return True
			
		except:
			print('ocorreu um erro no download:')
			raise
			exit()
		'''
		wget.download(self._link,nameFile)
		

url = 'https://dorynode.firebaseapp.com/v10.15.1_arm_release/node'	
node = Link(url)

#node.download('node')

#wget.download(url,'node')
'''
link = bs(rq.get('https://www.google.com/search?q=bs4+reference+pdf+python&oq=bs4+reference+pdf+python&aqs=chrome..69i57.7430j0j9&client=ms-android-motorola-rev2&sourceid=chrome-mobile&ie=UTF-8').text,'lxml').find_all('a')

for i in link:
	print(i.get('href'))
	
'''