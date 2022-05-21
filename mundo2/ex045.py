#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''Escolha sua opção:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual sua jogada: '))

print('=-'*10)
print(f'Você escolheu {itens[jogador]}')
print(f'O computador escolheu {itens[computador]}')
print('=-'*10)

print('JO')
sleep(1)
print('kEN')
sleep(1)
print('PO')

if computador == 0: #jogou pedra
    if jogador == 0:
        print('Empatou!!!!')
    elif jogador == 1:
        print('Você ganhou!!!')
    elif jogador == 2:
        print('O computador ganhou!!!')
    else:
        print('Jogada inválida!')
elif computador == 1: #jogou papel
    if jogador == 0:
        print('O computador ganhou!!!')
    elif jogador == 1:
        print('Empatou!!!!')
    elif jogador == 2:
        print('Você ganhou!!!')
    else:
        print('Jogada inválida!')
elif computador == 2:#jogou tesoura
    if jogador == 0:
        print('Você ganhou!!!')
    elif jogador == 1:
        print('O computador ganhou!!!')
    elif jogador == 2:
        print('Empatou!!!!')
    else:
        print('Jogada inválida!')





