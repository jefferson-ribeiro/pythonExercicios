# Exercício Python 48: Faça um programa que calcule a soma entre todos
# os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont += 1
print(f'Acabou, a soma dos {cont} número é o total de {soma}')
