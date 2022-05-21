print('=-='*15)
print('Analisador de Triângulos')
print('=-='*15)
r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os elementos acima PODEM FORMAR UM TRIÂNGULO')
else:
    print('Os elementos acima NÃO PODEM FORMAR UM TRIÂNGULO')



