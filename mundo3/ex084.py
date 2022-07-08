"""Exercício Python 084: faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No
final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. """

lista = []
pesado = 0
leve = 0
while True:
    pessoa = []
    nome = str(input('Digite o nome de uma pessoa: '))
    pessoa.append(nome)
    peso = int(input(f'Digite o peso da(o) {nome}: '))
    pessoa.append(peso)

    if len(lista) == 0:
        leve = peso
        pesado = peso

    if peso > pesado:
        pesado = peso

    if peso < leve:
        leve = peso

    lista.append(pessoa)
    sair = input('Deseja continuar? [S/N]').strip()[0]
    if sair in 'Nn':
        break
print(lista)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'Os mais pesadas pesam: {pesado}Kg e são:', end=' ')
for p in lista:
    if p[1] == pesado:
        print(p[0], end=' ')
print()
print(f'Os mais pesadas pesam: {leve}Kg e são:', end=' ')
for p in lista:
    if p[1] == leve:
        print(p[0], end=' ')
