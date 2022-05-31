# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite o sexo de uma pessoa: [M/F] ')).upper().strip()[0]
# while sexo not in 'MmFf': # outra forma de fazer
while sexo != 'M' and sexo != 'F':
    print(f'{sexo} inválido...')
    sexo = str(input('Digite o sexo de uma pessoa: [M/F] ')).upper().strip()[0]

print(f'O sexo escolido foi: {sexo}')
