salario = float(input('Digite o valor do seu salário atual para calcular o aumento R$ '))

if salario > 1250:
    aumento = salario +(salario/100)*10
else:
    aumento = salario + (salario / 100) * 15

print('Seu salário agora é: R$ {}'.format(aumento))
