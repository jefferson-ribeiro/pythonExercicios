from datetime import date

atual = date.today().year
nasc = int(input('Qual é o seu ano de nascimento?'))
idade = atual - nasc

print(f'Você tem {idade} anos em {atual}')