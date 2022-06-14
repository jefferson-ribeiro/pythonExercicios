from random import randint

"""Exercício Python 68: faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """

vitorias = 0
cont = 0
while True:
    print('====Vamos Jogar Par ou Ímpar=====')
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador} o total é {total}')
    cont += 1
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você perdeu!')
            break
        else:
            print('Você Venceu!')
            vitorias += 1
print(f'Você jogou {cont} vezes e venceu {vitorias}')