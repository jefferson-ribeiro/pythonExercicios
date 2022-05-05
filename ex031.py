viajem = float(input('Qual é a distância da sua viagem em km?'))

if viajem <= 200:
    valor = viajem * 0.50
else:
    valor = viajem * 0.45

print('O valor da sua viagem é R${}'.format(valor))