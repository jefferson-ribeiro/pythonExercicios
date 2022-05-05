velocidade = float(input('Qual é a velocidde atual do carro?'))

print('Tenha um bom dia dirija com segurança!')

if(velocidade <= 80):
    print('Parabens você está dentro da velocidade permitida')
else:
    print('ATENÇÃO!!! Você está acima da velocidade!')
    print('Sua multa é de R${:.2f}'.format((velocidade-80)*7))