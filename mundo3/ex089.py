"""Exercício Python 089: crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
cada aluno individualmente. """

lista = []

while True:
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input('Digite a primeira nota do aluno'))
    nota2 = float(input('Digite a segunda nota do aluno'))
    media = (nota1 + nota2) / 2
    lista.append([nome, nota1, nota2, media])
    sair = input('Deseja continuar? [S/N]').strip()[0]
    if sair in 'Nn':
        break

for i, aluno in enumerate(lista):
    print('#####-Boletim-#####')
    print(f'Aluno = {i}')
    print(f"nome: {aluno[0]}")
    print(f"média: {aluno[3]}")
    print('-------------------')

while True:
    aluno_notas = int((input('Deseja saber as notas de qual aluno: [digite o número]')))
    if aluno_notas <= len(lista):
        print(f'Nome: {lista[aluno_notas][0]}')
        print(f'Nota 1: {lista[aluno_notas][1]}')
        print(f'Nota 2: {lista[aluno_notas][2]}')
    else:
        print(f'O {aluno_notas} não existe!')
    sair = input('Deseja continuar? [S/N]').strip()[0]
    if sair in 'Nn':
        break
