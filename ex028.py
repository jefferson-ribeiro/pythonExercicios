from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'*20)
print('== Vou pensar em um número entre 0 e 5. Tente adivinhar... ==')
print('-=-'*20)
num = int(input('Em que número eu pensei?'))

print('Pensando.....')
sleep(2)

if(computador == num):
    print('Você ganhou eu também pensei no número {}'.format(computador))
else:
    print('Você perdeu :-( Eu pensei no número {}'.format(computador))
