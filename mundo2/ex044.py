#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

print('########### Produtos da LOJA ###########')

valor = float(input('Digite o valor da compra R$: '))

print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço formal ')
print('[4] 3x ou mais no cartão: 20% de juros')

opcao = int((input('Digite a forma de pagamento:')))

print(f'Valor da compra: R$ {valor}')
if opcao == 1:
    print(f'Pagamento à vista dinheiro/cheque: 10% de desconto: R$ {valor - ((valor/100)*10)}')
elif opcao == 2:
    print(f'Pagamento à vista no cartão: 5% de desconto R$ {valor - ((valor / 100) * 5)}')
elif opcao == 3:
    print(f'Pagamento: em até 2x no cartão, preço normal: 2 x de R$ {valor/2}')
elif opcao == 4:
    valor_juros = valor + (valor / 100) * 20
    print(f'Pagamento: 3x ou mais no cartão: 20% de juros: {valor_juros} ')
    parcelado = int(input('Digite em quantas vezes deseja parcelar: '))
    if parcelado < 3:
        print('O opção incorreta!')
    else:
        print(f'{parcelado}x de R$: {valor_juros/parcelado}')
else:
    print('opção inválida!!!!!!! TENTE NOVAMENTE!')