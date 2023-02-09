"""Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com
idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. """
from datetime import datetime

dados = dict()
dados['nome'] = input('digite o nome do trabalhador: ')
nasc = int(input('Digite o ano de nascimento XXXX: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('digite o número da carteira de trabalho: [0 = não tem]'))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contrataçao: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

for k, v in dados.items():
    print(f'{k}: {v}')
