import browser.browser as br

http = br.http()
https = br.https()

agent = 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'

url = 'http://sonharacordado.org.br/clubedossonhadores/'
nav = br.Browser()


nav.open(url, True)