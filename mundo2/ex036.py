casa = float(input('Valor da casa: R$ '))
salario = float(input('Valor do salário: R$ '))
tempo = int(input('Em quantos anos pretende pagar? '))

prestação = casa / (tempo * 12)
min = (salario*30)/100

print('O valor da prestação é R$ {:.2f}'.format(prestação))

if prestação <= min:
    print('APROVADO - você pode financiar!')
else:
    print('REPROVADO - você não pode financiar! A prestação deve ser no máximo R${:.2f}'.format(min))
