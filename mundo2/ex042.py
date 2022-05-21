# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('=-=' * 15)
print('Analisador de Triângulos')
print('=-=' * 15)
r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os elementos acima PODEM FORMAR UM TRIÂNGULO', end=' ')
    if r1 == r2 and r1 == r3:
        print('EQUILÁTERO: todos os lados iguais')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO: todos os lados diferentes')
    else:
        print('ISÓSCELES: dois lados iguais, um diferente')

else:
    print('Os elementos acima NÃO PODEM FORMAR UM TRIÂNGULO')
