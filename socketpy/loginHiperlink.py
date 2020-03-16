import mechanicalsoup

#declarations importantes
userAgent = 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'

http = 'http://144.217.161.146:8080'

https = 'https://50.237.232.151:1080'

name1 = 'SAMUEL'
name2 = 'MACEDO'
cpf = '08640684685'
email = 'legaaaaaalll@gmail.com'

#modifica os proxys de user
br = mechanicalsoup.StatefulBrowser()
br.session.proxies = {"http":http,"https":https} 
br.session.proxies.update({"http":http,"https":https})

#modifica os agentes de user
br.session.headers = {"User-Agent":userAgent} #
br.session.headers.update({"User-Agent":userAgent }) #Proxy


# abre o site
br.open('https://payments.wikimedia.org/index.php?title=Special:AstroPayGateway&appeal=JimmyQuote&ffname=astropay&recurring=false&utm_source=fr-redir.default%7Edefault%7Edefault%7Edefault%7Econtrol.cc&utm_medium=spontaneous&utm_campaign=spontaneous&utm_key=vw_360.vh_612.otherAmt_0.ptf_1.time_5&referrer=www.google.com%2F&language=pt-br&country=BR&payment_method=cc&payment_submethod=&gateway=&variant=&amountGiven=11.5&frequency=onetime&amount=Other&currency=BRL')

#verifica os form da pagina
print(br.get_current_page().find_all('form'))


#pega o form da pagina
form = br.select_form('form[name="payment"]')
print('vai')

#preenche os input do form
form.set('first_name', name1)
form.set('last_name', name2)
form.set('fiscal_number', cpf)
form.set('email', email)
form.set_radio({'payment_submethod': 'visa'})

#faz o envio e recebe os dados
res = br.submit_selected()
print(res.text)
print(res.url)

#pega o link recebido e reabre o trabalho
br.open(res.url)
print(br.get_current_page().find_all('form'))
form = br.select_form()
form.choice_submit()
res = br.submit_selected()
print(res.url)





#print(br.get_current_page().find_all('form'))
#print('foi')


#verificar se input foi editado ou nao

#resposta do login





#referer = 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) Gecko/41.0 Firefox/41.0'
#browser.get_current_form().print_summary()

#browser['school']= 'pooorra'

'''
print('foi')
br.select_form('form[action="/login"]')
print('foi')
br['school'] = 'pooorraaa'
br.launch_browser()
print('foi')
print(br.get_current_page())
'''

#browser.select_form('form[action="/login"]')