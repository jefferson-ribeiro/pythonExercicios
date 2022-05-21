d = float(input('Quantos dias alugados?'))
k = float(input('Quantos km rodados?'))

diaria = d*60
km = k*0.15

print('O total a pagar é R${:.2f}'.format(diaria+km))