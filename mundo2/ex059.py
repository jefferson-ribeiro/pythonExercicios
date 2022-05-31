# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.



num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('Qual é sua opção?'))

    if opcao == 1:
        print(f'{num1} + {num2} = {num1+num2}')
    elif opcao == 2:
        print(f'{num1} x {num2} = {num1*num2}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior número é: {maior}')
    elif opcao == 4:
        num1 = int(input('Digite um novo primeiro número: '))
        num2 = int(input('Digite um novo segundo número: '))
    elif opcao == 5:
        print('Obrigado até logo!')
    else:
        print(f'Opção {opcao} inválida!')

