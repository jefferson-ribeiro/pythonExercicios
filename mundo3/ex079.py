"""Exercício Python 079: crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente. """

lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Este número já existe e não será adicionado...')
    cont = input('Deseja continuar? [S/N]').strip()[0]
    if cont in 'Nn':
        break
print(f'Lista em ordem crescente: {sorted(lista)}')
