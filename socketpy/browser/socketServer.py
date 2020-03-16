import socket

class SockServer:
	def __init__(self, port, ip=socket.gethostname()):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((ip, port))
		self.ip = ip
		self.port = port
		self.s.listen(5)
		
		self.welcome = 'seja bem vindo seu arrombado' 
		print('server on')

	def recv(self, type='utf-8', bit=2048):
		msg = (self.clientsocket.recv(bit).decode(type))
		return msg
		
	def send(self, msg):
		self.clientsocket.send(msg.encode())
		
	def on(self, arrayComandsRes):
		print(f'o servidor {self.ip} está rodando na porta {self.port}')
		while True:
			self.clientsocket, self.address = self.s.accept()
			print(self.recv())		
			print(f'{self.clientsocket} stabilished connection')

			if self.recv() == arrayComandsRes[0]:
				print('feito')
				self.send(arrayComandsRes[1])
	
	
'''
comands = ['oi','fodaci seu arrombado']
radio = SockServer(12345)
print(comands[0])
radio.on(comands)
'''