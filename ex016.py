from math import trunc #importando somente funcção trunc dentro de math
num = float(input('digite um valor: '))
res = trunc(num)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, res))
