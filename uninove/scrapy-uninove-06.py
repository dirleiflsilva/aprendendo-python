# Buscando os icones da pagina pela tag <i>
import requests
from bs4 import BeautifulSoup

pagina = requests.get('http://www.uninove.br')
pagebs = BeautifulSoup(pagina.text, 'html.parser')

# encontra todos os icones
uninove = pagebs.find_all('i')

for i in uninove:
    print(i.prettify())

input('Tecle ENTER para sair...')