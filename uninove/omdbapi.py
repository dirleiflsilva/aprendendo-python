import requests
import json
 
def omdbapi (titulo):
    requisicao = requests.post('http://www.omdbapi.com/?apikey=fbc11b5a&t='+ titulo)
    return json.loads(requisicao.text)
 
filme = input('Nome do Filme em inglês (Braveheart): ')
if filme == '':
    filme = 'Braveheart'
 
dicionario = omdbapi(filme)
print('\nOMDB')
if (dicionario['Response']) == 'False':
    print('Filme não localizado')
else:
    print ('Ano de Produção: '+ dicionario['Year'])
    print ('Genero: '+ dicionario['Genre'])
    print ('Direção: '+ dicionario['Director'])
    atores = dicionario['Actors'].split(', ')
    printouator = False
    for ator in atores:
        if not printouator:
            print ('Ator: '+ ator)
            printouator = True
        else:
            print('    : '+ ator) 
    ratings = dicionario['Ratings']
    for rating in ratings:
        source = rating['Source']
        value = rating['Value']
        print('Fonte:',source +'. Valor:',value)