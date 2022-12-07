# Buscando os links da pagina pela tag <a>
import requests
from bs4 import BeautifulSoup

pagina = requests.get('http://www.uninove.br')
pagebs = BeautifulSoup(pagina.text, 'html.parser')

# encontra todos os links
uninove = pagebs.find_all('a')

for i in uninove:
    print(i.prettify())

input('Tecle ENTER para sair...')
