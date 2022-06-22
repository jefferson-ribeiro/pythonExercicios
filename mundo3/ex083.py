"""Exercício Python 083: crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu
aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. """

lista_abre = []
lista_fecha = []

expr = input('Digite uma expressão para verificação: ')

for item in expr:
    if item == '(':
        lista_abre.append(item)
    if item == ')':
        lista_fecha.append(item)
if len(lista_abre) == len(lista_fecha):
    print('Esta é um expressão válida!')
else:
    print('Esta expressão NÃO é válida!')
