import browser.socklib as s

t = s.Socket('google.com')
#t.send('oi')
#print(t.recv()
t.send_http('search?q=sexo')
print(t.recv())
t.pingNet(100)