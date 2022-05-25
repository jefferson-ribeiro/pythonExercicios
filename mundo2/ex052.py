# Exercício Python 52: Faça um programa que leia um número
# inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))

tot = 0
for n in range(1, numero + 1):
    if numero % n == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{n}', end='')
print(f'\n\033[mO número {numero} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')



