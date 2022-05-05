import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
himat = (co ** 2 + ca **2) **(1/2)
hi = math.hypot(co, ca)

print('Calculo matemático: A hipotenusa vai medir {:.2f}'.format(himat))
print('Calculo import: A hipotenusa vai medir {:.2f}'.format(hi))
