# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor =0
for pessoa in range(1, 8):
    nasc = int(input(f'Digite em que ano a pessoa {pessoa}º nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Existem {totmaior} pessoas maiores de idade')
print(f'Existem {totmenor} pessoas menores de idade')
