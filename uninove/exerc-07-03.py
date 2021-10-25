# divisão por dois números
# com tratamento exceção!
try:
    numero1 = int(input('Entre com o primeiro número: '))
    numero2 = int(input('Entre com o segundo número: '))

    resultado = numero1 / numero2
    print('O resultado é: ',resultado)
except ValueError:
    print('Valor inválido!')
except ZeroDivisionError:
    print('Não é possível divisão por zero')
input('Pressione ENTER para sair...')
