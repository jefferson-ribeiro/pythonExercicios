"""
Exercício Python 075: desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares
"""

num = (int(input('Digite um número:')), int(input('Digite outro número:')),
       int(input('Digite mais um número:')), int(input('Digite o último número:')))
print(f'Segue a tupla digitada: {num}')
print(f'O número nove(9) apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número três(3) apareceu na posição {num.index(3)}')
else:
    print('Número 3(três) não encontrado')
print(f'Segue os números pares encontrados: ')
for n in num:
    if n % 2 == 0:
        print(n)
