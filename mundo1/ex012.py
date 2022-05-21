preco = float(input('Qual é o valor do produto? R$'))
desc = preco - (preco*0.05)

print('O produto no valor de R${:.2f} com 5% de desconto fica no valor de R${:.2f}'.format(preco,desc))