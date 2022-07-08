"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. """

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
coluna3 = 0
maior_linha2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input("Digite um número: "))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        coluna3 += matriz[l][2]
        if c == 0 or matriz[1][c] > maior_linha2:
            maior_linha2 = matriz[1][c]

for l in range(0, 3):
    for c in range(0, 3):
        print([matriz[l][c]], end='')
    print()

print(f'A soma de todos os valores pares digitados é: {soma}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {maior_linha2}')
