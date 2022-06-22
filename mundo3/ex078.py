"""Exercício Python 078: faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """

cont = 0
lista = []
menor = 0
maior = 0
while cont != 5:
    numero = int(input(f'Digite o {cont+1}º numero: '))
    lista.append(numero)
    if cont == 0:
        menor = numero
        maior = numero
    else:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
    cont += 1
print(f'Lista de números: {lista}')
print(f'O maior número da lista é o {max(lista)}')
print(f'O menor número da lista é o {min(lista)}')

print('='*20)
print('Nas posições: ', end=' ')
for i, n in enumerate(lista):
    if n == maior:
        print(f'{i}, ', end=' ')
print(f'- O maior número da lista é o {maior}')

print('Nas posições: ', end='')
for i, n in enumerate(lista):
    if n == menor:
        print(f'{i}, ', end=' ')
print(f'- O menor número da lista é o {menor}')
