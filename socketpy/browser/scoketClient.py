from socklib import Socket as s

test = s('localhost',1234)
test.send('oi')
print(test.recv())


'''
#user = input('digite teu nome: ')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((socket.gethostname(), 1234))
except:
	print('erro na conexão!, olha a porra do proxy q vc colocou  arrombado')
	exit()


def send(msg):
	s.send(bytes(msg, 'utf-8'))

def recv():
	mg = s.recv(1024)
	print(mg.decode('utf-8'))
	
#while True:
recv()
'''