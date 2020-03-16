import browser.socklib as s
import time
from colorama import *
import browser.irc as i

irc = i.Irc
nick = 'jezuis_matrix'
user = 'jezuis'
irc = irc(user, nick)
#save = irc.save()

mg = ''
while True:
	#time.sleep(1)
	msg = (irc.recv())
	if(msg!=mg):
		print(msg)
		irc.save(msg,'chat.txt')
		try:
					if(msg.index('brazil') > -1):
						irc.save(msg, 'br.txt')
						print(Fore.YELLOW+msg)
						print(Style.RESET_ALL)
		except:
			pass
		#salvando aprovada 
		try:
			if(msg.index('APROVADA') > -1 or msg.index('aproved') > -1):
				irc.save(msg, 'cc.txt')
				print(Fore.GREEN+msg)
				print(Style.RESET_ALL)
			
		except:
			pass
		irc.hi(msg)
		irc.checa_ping(msg)
	else:
		pass	
	mg = msg

	
