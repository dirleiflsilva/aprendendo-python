# Buscando apenas parte dos paragrafos da pagina pela tag <p>
import requests
from bs4 import BeautifulSoup

pagina = requests.get("http://www.uninove.br")
pagebs = BeautifulSoup(pagina.content, 'html.parser')

# indice 2, terceira posicao
print(pagebs.find_all('p')[2].get_text())
# indice 4, quinta posicao
print(pagebs.find_all('p')[4].get_text())

input('Tecle ENTER para sair...')