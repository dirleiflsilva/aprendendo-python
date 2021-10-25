# Buscando os titulos da pagina pela tag <h1>
import requests
from bs4 import BeautifulSoup

pagina = requests.get('http://www.uninove.br')
pagebs = BeautifulSoup(pagina.text, 'html.parser')

# encontra todos os titulos
uninove = pagebs.find_all('h1')

for i in uninove:
    print(i.prettify())

input('Tecle ENTER para sair...')