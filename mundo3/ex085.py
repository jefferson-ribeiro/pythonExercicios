"""Exercício Python 085: crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
crescente. """

lista = [[], []]

for c in range(0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print(f'Segue lista de valores pares em ordem crescente: {sorted(lista[0])}')
print(f'Segue lista de valores ímpares em ordem crescente: {sorted(lista[1])}')
