# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date

nasc = int(input('Digite o ano de nascimento do atleta: '))

ano_atual = date.today().year

idade = ano_atual - nasc

print(f'Idade do alteta: {idade} anos')
if idade <= 9:
    print('Até 9 anos: MIRIM')
elif idade > 9 and idade <= 14:
    print('Até 14 anos: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Até 19 anos: JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Até 25 anos: SÊNIOR')
else:
    print('Acima de 25 anos: MASTER')
