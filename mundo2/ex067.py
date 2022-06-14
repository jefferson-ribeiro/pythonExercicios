"""Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. """

while True:
    num = int(input('Digite um número para mostrar sua tabuada: '))
    if num < -1:
        break
    print(f'=====- TABUADA DO {num} -=====')
    for n in range(1, 11):
        print(f'{num} x {n} = {n * num}')
print('Programa finalizado!')
