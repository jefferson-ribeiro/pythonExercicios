# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
maioridadehomem = 0
nomevelho = ''

for p in range(1, 5):
    nome = str(input(f'Digite o nome da {p}º pessoa: ').strip())
    idade = int(input(f'Digite a idade da {p}º pessoa'))
    somaidade += idade
    sexo = str(input(f'Digite o sexo da {p}º pessoa (M/F)').strip())
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
print(f'A média de idade do grupo é {somaidade / 2}')
print(f'O nome do homem mais velho é {nomevelho} que tem {maioridadehomem} anos')