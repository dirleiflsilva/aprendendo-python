# Scrap x Crawler - diferenca tenue
import urllib.request
from bs4 import BeautifulSoup
url = urllib.request.urlopen('http://www.uninove.br').read()
pageurl = BeautifulSoup(url, 'lxml')
print(pageurl.h1.text)
input('Pressione ENTER para sair...')