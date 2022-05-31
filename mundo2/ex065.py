# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = 0
res = 's'
soma = 0
cont = 0
maior = 0
menor = 0
while res in 'Ss':
    num = int(input('Digite um número'))
    res = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Você digitou {cont} números, e a média dos valores é {soma/cont} ')
print(f'O maior valor é {maior} e o menor valor é {menor}')
print('Acabou!!!')