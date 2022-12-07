
fontes_27 = open('RPO-12.1.27-nome.txt','r').read().split('\n')
fontes_33 = open('RPO-12.1.33-nome.txt','r').read().split('\n')

fontes_27 = fontes_27.upper()
fontes_33 = fontes_33.upper()

print(len(fontes_33))

conjunto_27 = set(fontes_27) 
conjunto_33 = set(fontes_33)
print(len(conjunto_33))

fontes_33_27 = conjunto_33.intersection(fontes_27)
# print(len(fontes_33_27))
# print(fontes_33_27)

dif_fontes_33_27 = conjunto_33.difference(fontes_27)
# print(len(dif_fontes_33_27))
# print(dif_fontes_33_27)

fontes_27_33 = conjunto_27.intersection(fontes_33)
print(len(fontes_27_33))
# print(fontes_27_33)

dif_fontes_27_33 = conjunto_27.difference(fontes_33)
# print(len(dif_fontes_27_33))
# print(dif_fontes_33_27)

#with open('lista_fontes_27_33','w+') as f:
#    for lista in fontes_27_33:
#        f.write('%s\n' %lista)
#f.close()

"""
with open('lista_fontes_33','w+') as f:
    for lista in fontes_33:
        f.write('%s\n' %lista)
f.close()

with open('lista_fontes_33_27','w+') as f:
    for lista in fontes_33_27:
        f.write('%s\n' %lista)
f.close()

with open('lista_dif_fontes_33_27','w+') as f:
    for lista in dif_fontes_33_27:
        f.write('%s\n' %lista)
f.close()
"""
