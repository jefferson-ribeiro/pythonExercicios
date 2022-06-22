"""Exercício Python 080: crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela. """

lista = []
for x in range(0, 5):
    i = int(input(f'Digite o {x + 1}º valor: '))
    if x == 0 or i >= lista[-1]:
        lista.append(i)
        print('Adicionado ao fim da lista.')
    else:
        for y in lista:
            if y >= i:
                lista.insert(lista.index(y), i)
                print(f'Adicionado na posição {lista.index(i)} da lista.')
                break

print(f'Os valores digitados em ordem foram {lista}')
