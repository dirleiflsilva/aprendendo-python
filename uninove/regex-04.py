import re
import requests

requisicao = requests.post('https://www.uninove.br/graduacao/ciencia-da-computacao/fale-com-o-coordenador/')
string_de_retorno = requisicao.text
 
padrao = re.findall(r'mailto:\w[\w\.-]+@[\w-]+\.[\w\.-]*\w{2,3}',string_de_retorno)
for x in padrao:
    print(x)
    comprimento = len(x)
    print (x[7:comprimento])
