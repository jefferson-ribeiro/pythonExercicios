# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial

numero = int(input('Digite um número para calcular o seu fatorial:'))
f = 1  # factorial(numero)


#print(f'O Fatorial de {numero} é {f}')

print('###Fazendo pelo modo tradicional###')
c = numero
print(f'Calculando {numero}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
