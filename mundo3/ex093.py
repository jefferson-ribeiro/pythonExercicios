"""Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. """

jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
partidas = [int(input(f'Digite quantos gols fez na partida{i + 1} ')) for i in range(0, tot)]
jogador['gols'] = partidas
jogador['total'] = sum(partidas)
print('=*'*20)
print(jogador)
print('=*'*20)
for c, v in jogador.items():
    print(f'O campo {c} tem o valor: {v}')
print('=*'*20)
print(f'O jogador {jogador["nome"]}, jogou {tot} partidas')
cont = 0
while cont != tot:
    print(f'Na partida {cont+1}, fez {jogador["gols"][cont]} gols')
    cont += 1