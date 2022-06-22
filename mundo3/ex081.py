"""Exercício Python 081: crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
 A) Quantos números foram digitados.
 B) A lista de valores, ordenada de forma decrescente.
 C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
cont = 0
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    cont += 1
    sair = input('Deseja continuar? [S/N]').strip()[0]
    if sair in 'Nn':
        break
print(f'Foram digitados {cont} números')
print(f'Lista em ordem decrescente: {sorted(lista, reverse = True)}')

if 5 in lista:
    print('O valor 5 (cinco) está na lista')
else:
    print('O valor 5 (cinco) NÃO está na lista')

