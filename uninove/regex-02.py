import re
 
string = 'O aluno José foi reprovado. Ele tirou 10.0 na segunda nota'
procurar = re.search(r'\w\w\w\w\w\w',string)
if procurar:
    print(procurar.group())
else:
    print('Não encontrado!')
 
procurar = re.search(r'\d',string)
if procurar:
    print(procurar.group())
else:
    print('Não encontrado!')
 
procurar = re.search(r'\w\w\w\w\w\w+',string)
if procurar:
    print(procurar.group())
else:
    print('Não encontrado!')
 
procurar = re.search(r'\w{6,8}',string)
if procurar:
    print(procurar.group())
else:
    print('Não encontrado!')
 
 
procurar = re.search(r'\w{5}\w+',string)
if procurar:
    print(procurar.group())
else:
    print('Não encontrado!')
 
procurar = re.search(r'\d+',string)
if procurar:
    print(procurar.group())
else:
    print('Não encontrado!')

procurar = re.search(r"\d+\.\d+",string)
if procurar:
    print(procurar.group())
else:
    procurar = re.search(r"\d+", string)
    if procurar:
        print(procurar.group())
    else:
        print("Não encontrado!")    
