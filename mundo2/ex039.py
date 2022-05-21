from datetime import date

atual = date.today().year
nasc = int(input('Qual é o seu ano de nascimento?'))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')

if idade == 18:
    print('Deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} para você deve se alistar')
    print(f'Seu alistamento será no ano de {nasc + 18}')
elif idade > 18:
    print(f'Você tem {idade} anos, já deveria ter se alistado há {idade-18} anos')
    print(f'Seu alistamento foi no ano de {nasc + 18}')
