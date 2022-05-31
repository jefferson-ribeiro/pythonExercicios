# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

computador = randint(0, 5)
contador = 1

print('-=-' * 20)
print('== Vou pensar em um número entre 0 e 5. Tente adivinhar... ==')
print('-=-' * 20)

num = int(input('Em que número eu pensei?'))
print('Pensando.....')
sleep(2)

while num != computador:
    if computador > num:
        print(f'O meu número é maior que {num}')
    elif computador < num:
        print(f'O meu número é menor que {num}')
    num = int(input('Tente novamente... Em que número eu pensei?'))
    print('Pensando.....')
    sleep(2)
    contador += 1

print(f'Você tentou {contador} vezes')
print('Você ganhou eu também pensei no número {}'.format(computador))
