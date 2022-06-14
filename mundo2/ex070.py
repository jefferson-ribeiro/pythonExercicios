"""Exercício Python 70: crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

total = 0.0
p_mil = 0
barato = 0
nome_barato = ''
cont = 0

while True:
    nome = input('Digite o nome do produto: ')
    preco = int(input(f'Digite o preco do {nome}'))
    cont += 1
    if cont == 1 or preco < barato:
        barato = preco
        nome_barato = nome
    if preco >= 1000:
        p_mil += 1
    sair = input('Deseja cadastrar novo produto? [S/N]')
    total += preco
    if sair in 'Nn':
        break

print(f'O valor total de produtos é R${total}')
print(f'O pedido tem {p_mil} produtos acima de R$ 1.000,00')
print(f'O produto mais barato é {nome_barato} {barato}')


