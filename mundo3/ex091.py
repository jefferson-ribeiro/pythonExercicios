"""Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde
esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
o maior número no dado. """
import random
from operator import itemgetter
num = 1
jogadores = dict()

for j in range(0, 4):
    nome = input(f'Digite o nome do jogador {num}: ')
    dado = random.randint(1, 6)
    jogadores.update({nome: dado})
    num += 1

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar - {v[0]} com {v[1]} pontos')
