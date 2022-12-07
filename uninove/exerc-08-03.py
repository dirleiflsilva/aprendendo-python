# valida o número do cpf com apenas números
import re
cpf = str(input('Entre com o número do CPF, com apenas números: \n'))
if re.search('\d{11}', cpf):
    print('Número CPF validado')
else:
    print('Número do CPF fora do padrão')
input('Pressione ENTER para sair...')
