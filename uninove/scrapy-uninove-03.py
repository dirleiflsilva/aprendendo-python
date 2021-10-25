# Buscando os paragrafos da pagina pela tag <p>
import requests
from bs4 import BeautifulSoup

pagina = requests.get('http://www.uninove.br')

pagebs = BeautifulSoup(pagina.text, 'html.parser')

# encontra todos os paragrafos
uninove = pagebs.find_all('p')

for i in uninove:
    print(i.prettify())

input('Tecle ENTER para sair...')