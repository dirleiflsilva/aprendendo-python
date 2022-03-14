import re
 
string = 'O aluno José foi reprovado. Ele tirou 7.7 na segunda nota'
 
procurar = re.findall(r'\w\w\w\w+',string)
if procurar:
    for x in procurar:
        print(x)
else:
    print('Não encontrado!')
