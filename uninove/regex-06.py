import re

string = 'C3PO é um Robo. R2D2 também é. XR é smartphone.'
procurar = re.search(r'[\w\d]+R[\w\d]*',string)

if (procurar):
    print(procurar.group())
else:
    print('Não encontrado!')
