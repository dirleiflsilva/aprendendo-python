import re

string = 'Aluno tirou 10. U2 é sua banda favorita.'
procurar = re.search(r'\w\d',string)

if (procurar):
    print(procurar.group())
else:
    print('Não encontrado')
