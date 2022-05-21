# Exercício Python 040:
# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

def print_media(n1, n2):
    media = (n1 + n2) / 2
    print(f'A média entre as notas {n1} e {n2} é: {media}')
    if media < 5:
        print(f'A média entre as notas {n1} e {n2} é: {media}')
        print('Média abaixo de 5.0: REPROVADO')
    elif 5 <= media <= 6.9:
        print('Média entre 5.0 e 6.9: RECUPERAÇÃO')
    else:
        print('Média 7.0 ou superior: APROVADO')


n1 = (float(input('Digite a primeira nota do aluno: ')))
n2 = (float(input('Digite a segunda nota do aluno: ')))

print_media(n1, n2)
