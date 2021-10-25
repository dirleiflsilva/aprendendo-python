# valida o número do cpf com apenas com hífen
import re
cpf = str(input('Entre com o número do CPF, apanes com hífen: \n'))
if re.search('\d{3}\d{3}\d{3}-\d{2}', cpf):
    print('Número CPF validado')
else:
    print('Número do CPF fora do padrão')
input('Pressione ENTER para sair...')
