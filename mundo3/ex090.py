"""Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela. """

aluno = dict()

aluno['nome'] = input("Digite o nome do aluno: ")
aluno['media'] = float(input('Digite a media do aluno: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado!'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'recuperação!'
else:
    aluno['situação'] = 'reprovado!'

print("-_-"*10)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')