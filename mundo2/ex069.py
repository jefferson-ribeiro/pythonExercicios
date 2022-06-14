"""Exercício Python 69: crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

pessoas18 = 0
homens = 0
mulheres_menos_d20 = 0

while True:
    idade = int(input('Informe a idade a ser cadastrada: '))
    sexo = input('Informe o sexo a ser cadastrado: ')
    if idade >= 18:
        pessoas18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres_menos_d20 += 1
    continuar = input('Deseja continuar? [S/N]').upper()[0]
    if continuar in 'N':
        break
print(f'{pessoas18} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres_menos_d20} mulheres tem menos de 20 anos.')