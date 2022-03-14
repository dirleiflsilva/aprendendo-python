import re
 
string = 'O aluno José foi reprovado. A aluna Ana foi aprovada e os alunos Thiago e Andre ficaram em dependência'
 
procurar = re.match('O aluno',string)
print(procurar)
procurar = re.match('Ana',string)
print(procurar)
procurar = re.search('O aluno',string)
print(procurar)
procurar = re.search('Ana',string)
print(procurar)
procurar = re.search('Monica',string)
print(procurar)
