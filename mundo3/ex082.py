"""Exercício Python 082: crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao
final, mostre o conteúdo das três listas geradas. """
lista_geral = []
lista_pares = []
lista_impares = []

while True:
    lista_geral.append(int(input('Digite um número: ')))
    sair = input('Deseja continuar? [S/N]').strip()[0]
    if sair in 'Nn':
        break

print(f'Lista geral: {lista_geral}')

for n in lista_geral:
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

print(f'Lista somente com números pares {lista_pares}')
print(f'Lista somente com números impares {lista_impares}')
