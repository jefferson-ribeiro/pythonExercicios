"""Exercício Python 074: crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois
disso, mostre a listagem de números gerados e também indique o menor e o maior valor na tupla. """
from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Números sorteados: {numeros}')
print(f'O maior número é : {max(numeros)}')
print(f'O menor número é : {min(numeros)}')
